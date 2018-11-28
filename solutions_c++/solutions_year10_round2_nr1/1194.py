#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <ctime>
#include <set>

//Standard utilities
using namespace std;
vector<string>* Tokenize(const string& str, const string& delimiters = ",");
template<class T> string toString(const T& t);
template<class T> T fromString(const string& s);
class timer;


//=============================================================================
//=============================================================================
int mkdir(set<string>* dirs, string path, unsigned int curPath = 0)
{
	int outCount = 0;
	if (string::npos != curPath )
	{
		unsigned int end = path.find_first_of("/", curPath+1);
		//add the dir
		pair<set<string>::iterator,bool> added = dirs->insert(path.substr(0, end));
		outCount += added.second;
		if (string::npos != end )
		{//this dir existed, try the next
			outCount += mkdir(dirs,path,end);
		}
	}
	return outCount;
}

int main()
{
	string FileName = "A-large";
	ifstream inFile;
	ofstream outFile;
	string inBuffer, outBuffer;
	vector<string>* tokens;
	int N, n;
	inBuffer = outBuffer = "";
	N = n = 0;
	
	//Initialize

	//Solve
	outFile.open((FileName + ".out").c_str(), ios_base::out);
	inFile.open((FileName + ".in").c_str(), ios_base::in);
	if(inFile.good())
	{
		getline(inFile,inBuffer);//Grab the number of expected cases
		N = fromString<int>(inBuffer);
	}else{
		cout << "\nTERMINAL ERROR: Bad input file!\n";
		system("PAUSE");
		return 0;
	}
	while(inFile.good() && (n < N))
	{
		set<string>* dirs = new set<string>();
		n++;
		outBuffer = "";
		int oldCount = 0;
		int newCount = 0;
		string dir;
		int counter = 0;
		//Load Case Data
		{
			getline(inFile,inBuffer);
			tokens = Tokenize(inBuffer," ");
			oldCount = fromString<int>(tokens->at(0));
			newCount = fromString<int>(tokens->at(1));
			delete tokens;
			while(oldCount)
			{
				--oldCount;
				getline(inFile,dir);
				mkdir(dirs,dir);
			}
		}
		//Solve Case
		{
			while(newCount)
			{
				--newCount;
				getline(inFile,dir);
				counter += mkdir(dirs,dir);
			}
		}
		//Output Case Solution
		{
			cout << "Case #" << n << ": " << counter << endl;
			outFile << "Case #" << n << ": " << counter << endl;
		}
		dirs->clear();
		delete dirs;
	}
	inFile.close();
	system("PAUSE");
	return 0;
}







//=============================================================================
//=============================================================================
vector<string>* Tokenize(const string& str, const string& delimiters)
{
	vector<string>* tokens = new vector<string>();
	string::size_type lastPos = str.find_first_not_of(delimiters, 0); // Skip delimiters at beginning.
	string::size_type pos = str.find_first_of(delimiters, lastPos); // Find first "non-delimiter".
	
	while (string::npos != pos || string::npos != lastPos)
	{
		// Found a token, add it to the vector.
		tokens->push_back(str.substr(lastPos, pos - lastPos));
		// Skip delimiters.  Note the "not_of"
		lastPos = str.find_first_not_of(delimiters, pos);
		// Find next "non-delimiter"
		pos = str.find_first_of(delimiters, lastPos);
	}
	return tokens;
}

template<class T> string toString(const T& t)
{
	ostringstream stream;
	stream << t;
	return stream.str();
}

template<class T> T fromString(const string& s)
{
	istringstream stream (s);
	T t;
	stream >> t;
	return t;
}



//=============================================================================
//timer Class from http://sites.google.com/site/jivsoft/Home/timer
//=============================================================================
class timer
{
 private:
  bool running;
  clock_t start_clock;
  time_t start_time;
  double acc_time;

  double elapsed_time();

 public:
  // 'running' is initially false.  A timer needs to be explicitly started
  // using 'start' or 'restart'
  timer() : running(false), start_clock(0), start_time(0), acc_time(0) { }

  void start(const char* msg = 0);
  void restart(const char* msg = 0);
  void reset(const char* msg = 0);
  void stop(const char* msg = 0);
  void check(const char* msg = 0);
  friend ostream& operator<<(ostream& os, timer& t);

}; // class timer

//===========================================================================
// Return the total time that the timer has been in the "running"
// state since it was first "started" or last "restarted".  For
// "short" time periods (less than an hour), the actual cpu time
// used is reported instead of the elapsed time.

inline double timer::elapsed_time()
{
  time_t acc_sec = time(0) - start_time;
  if (acc_sec < 3600)
    return (clock() - start_clock) / (1.0 * CLOCKS_PER_SEC);
  else
    return (1.0 * acc_sec);

} // timer::elapsed_time

//===========================================================================
// Start a timer.  If it is already running, let it continue running.
// Print an optional message.

inline void timer::start(const char* msg)
{
  // Print an optional message, something like "Starting timer t";
  if (msg) std::cout << msg << std::endl;

  // Return immediately if the timer is already running
  if (running) return;

  // Set timer status to running and set the start time
  running = true;
  start_clock = clock();
  start_time = time(0);

} // timer::start

//===========================================================================
// Turn the timer off and start it again from 0.  Print an optional message.

inline void timer::restart(const char* msg)
{
  // Print an optional message, something like "Restarting timer t";
  if (msg) std::cout << msg << std::endl;

  // Set timer status to running, reset accumulated time, and set start time
  running = true;
  acc_time = 0;
  start_clock = clock();
  start_time = time(0);

} // timer::restart

//===========================================================================
// Stop the timer and print an optional message.

inline void timer::stop(const char* msg)
{
  // Print an optional message, something like "Stopping timer t";
  if (msg) std::cout << msg << std::endl;

  // Compute accumulated running time and set timer status to not running
  if (running) acc_time += elapsed_time();
  running = false;

} // timer::stop

//===========================================================================
// Resets the timer without changing the running state and print an optional message.

inline void timer::reset(const char* msg)
{
  // Print an optional message, something like "Stopping timer t";
  if (msg) std::cout << msg << std::endl;

  // Compute accumulated running time and set timer status to not running
  acc_time = 0;

} // timer::reset

//===========================================================================
// Print out an optional message followed by the current timer timing.

inline void timer::check(const char* msg)
{
  // Print an optional message, something like "Checking timer t";
  if (msg) std::cout << msg << " : ";

  std::cout << "Elapsed time [" << std::setiosflags(std::ios::fixed)
            << std::setprecision(2)
            << acc_time + (running ? elapsed_time() : 0) << "] seconds\n";

} // timer::check

//===========================================================================
// Allow timers to be printed to ostreams using the syntax 'os << t'
// for an ostream 'os' and a timer 't'.  For example, "cout << t" will
// print out the total amount of time 't' has been "running".

inline std::ostream& operator<<(std::ostream& os, timer& t)
{
  os << std::setprecision(2) << std::setiosflags(std::ios::fixed)
    << t.acc_time + (t.running ? t.elapsed_time() : 0);
  return os;
}

//===========================================================================
