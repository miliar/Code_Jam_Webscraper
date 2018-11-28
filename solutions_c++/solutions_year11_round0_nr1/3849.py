#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;


class Robot {
public:
   int currPos;
   int targetPos;
   int sequence;
};

class FileReader {
public:
   FileReader() {}
   bool openFile(string);
   int readInt();
   string readString();
   long readLong();
   char readChar();
   float readFloat();

   void close();
   ~FileReader(){}

private:
   ifstream mystream;
};

bool FileReader::openFile(string fn) {
   if(mystream.is_open())
      mystream.close();

   mystream.open(fn.c_str());
   return mystream.is_open();
   
}

int FileReader::readInt() {
   int val;
   mystream >> val;

   return val;
}

string FileReader::readString() {
   string val;
   getline(mystream, val);

   return val;
}

long FileReader::readLong() {
   long val;
   mystream >> val;

   return val;
}

char FileReader::readChar() {
   char val;
   mystream >> val;

   return val;
}

float FileReader::readFloat() {
   float val;
   mystream >> val;

   return val;
}

void FileReader::close() {
   mystream.close();
}

class FileWriter {
public:
   bool openFile(string fn);
   void writeString(string);
   void writeInt(int);
   void endLine();
   void close();

private:
   ofstream mystream;
};

bool FileWriter::openFile(string fn) {
   if(mystream.is_open())
      mystream.close();

   mystream.open(fn.c_str());
   return mystream.is_open();
   
}

void FileWriter::writeString(string s) {
   mystream << s;
}

void FileWriter::writeInt(int val) {
   mystream << val;
}

void FileWriter::endLine() {
   mystream << endl;
}

void FileWriter::close() {
   mystream.close();
}

class Algorithm {
public:
   void run(FileReader&, FileWriter&);
   int calculateTime(Robot*, Robot*, int,int);

private:
  void init(FileReader&, FileWriter&); 
};

void Algorithm::run(FileReader& in, FileWriter& out) {
   init(in, out);
}

int Algorithm::calculateTime(Robot *O, Robot *B, int oc, int bc) {
   int time=0;
   int i=0,j=0;
   int seq=1;
   bool pushedButton;
   bool bpushed=false;
   bool opushed = false;
   while(i < oc && j < bc) {
      pushedButton = false;
      //check O robot move
      opushed = false;
     if(O[i].currPos < O[i].targetPos)
	O[i].currPos = O[i].currPos + 1; 
     else if(O[i].currPos > O[i].targetPos)
       O[i].currPos = O[i].currPos - 1;
     else if(O[i].sequence == seq) {
         i++;
	 time++;
	 seq++;
	 pushedButton = true;
	 opushed = true;
	 //check B robot move
     	/*if(B[j].currPos < B[j].targetPos)
	   B[j].currPos = B[j].currPos + 1; 
     	else if(B[j].currPos > B[j].targetPos)
           B[j].currPos = B[j].currPos - 1;*/
	 //continue;
     } 

     //check B robot move
     bpushed = false;
     if(B[j].currPos < B[j].targetPos)
	B[j].currPos = B[j].currPos + 1; 
     else if(B[j].currPos > B[j].targetPos)
       B[j].currPos = B[j].currPos - 1;
     else if(B[j].sequence == seq) {
         j++;
	 time++;
	 seq++;
	 pushedButton = true;
	 bpushed = true;
	 if(O[i].currPos < O[i].targetPos && opushed)
	   O[i].currPos = O[i].currPos + 1; 
     	else if(O[i].currPos > O[i].targetPos && opushed)
           O[i].currPos = O[i].currPos - 1;  
     } 
     if(!pushedButton)
        time++;
   }

   // O robot remaining move if any
   while (i < oc) {
      if(O[i].currPos < O[i].targetPos)
	O[i].currPos = O[i].currPos + 1; 
     else if(O[i].currPos > O[i].targetPos)
       O[i].currPos = O[i].currPos - 1;
     else if(O[i].sequence == seq) {
         i++;
	 time++;
	 seq++;
	 continue;
     } 
     time++;
   }

   //B robot remaining move if any
   while(j < bc) {
      if(B[j].currPos < B[j].targetPos)
	B[j].currPos = B[j].currPos + 1; 
     else if(B[j].currPos > B[j].targetPos)
       B[j].currPos = B[j].currPos - 1;
     else if(B[j].sequence == seq) {
         j++;
	 time++;
	 seq++;
	 continue;
     } 
     time++;
   }

   return time;
}

void Algorithm::init(FileReader& in, FileWriter& out) {
   int testcase;
   int i,j;
   int button;
   string output;
   int result;
   Robot Orobot[100], Brobot[100];
   int Ocount,Bcount;

   testcase = in.readInt();
   cout << testcase << endl;
   for(i=0;i<testcase;i++) {
       button=in.readInt();
       cout << button;
       Ocount=0;
       Bcount=0;
       for(j=0;j<button;j++) {
	   char ch;
	   int val;
	   //in.readChar();
	   ch = in.readChar();
	   //in.readChar();
	   val=in.readInt();
	   cout <<"-" << ch <<"-"<<val;
	   if(ch == 'O') {
	      Orobot[Ocount].currPos = (Ocount?Orobot[Ocount-1].targetPos:1);
	      Orobot[Ocount].targetPos=val;
	      Orobot[Ocount].sequence = j+1;
	      Ocount++;
           }
	   else {
	      Brobot[Bcount].currPos = (Bcount?Brobot[Bcount-1].targetPos:1);
	      Brobot[Bcount].targetPos=val;
	      Brobot[Bcount].sequence = j+1;
	      Bcount++;
	   }
       }
       result =  calculateTime(Orobot, Brobot, Ocount, Bcount);
       cout << "Required Time: " << result << endl;   
       output.clear();
       out.writeString("Case #");
       out.writeInt(i+1);
       out.writeString(": ");
       out.writeInt(result);
       out.endLine();
   }
}

int main() {
  int choice;
  string filename;
  FileReader fr;
  FileWriter fw;
  Algorithm alg;
  //cout << "Hello" << endl;
  
  do {
     cout << "\n\n\n1. Input File" << endl;
     cout << "2. Output File" << endl;
     cout << "3. Run" << endl;
     cout << "4. Exit" << endl;

     cout << "\nEnter Your Choice: ";
     cin >> choice;

     switch(choice) {
        case 1:
	   cout << "Enter the input file name: ";
	   cin.ignore();
	   getline(cin, filename);

	   if(!fr.openFile(filename))
	      cout<< "File opening error" << endl;
	   break;

	case 2:
	   cin.ignore();
           cout << "Enter the output file name: ";
	   getline(cin, filename);

	   if(!fw.openFile(filename))
	      cout<< "File opening error" << endl;
	   break;
	case 3:
	   alg.run(fr, fw);
	   fr.close();
	   fw.close();
	   break;

	case 4:
	   cout << "Exiting the program..." << endl;
	   break;
	default:
	   cout << "\n\nERROR: Invalid Choice!!!" << endl;
     }

  } while(choice != 4);

  return 0;
}
