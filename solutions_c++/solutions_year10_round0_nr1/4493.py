#include <iostream>
#include <fstream>

#define INPUT_FILE_PATH		"C:\\Projects\\CodeJam\\Test\\in.txt"
#define OUTPUT_FILE_PATH	"C:\\Projects\\CodeJam\\Test\\out.txt"

using namespace std;

void go();


int main()
{
	try
	{
		go();
	}
	catch(...)
	{
		cerr << "Exception caught!!!" << endl;
		return 1;
	}

	return 0;
}

void go()
{
	ifstream in_file;
	ofstream out_file;

	in_file.open(INPUT_FILE_PATH);
	if(!in_file.is_open())
	{
		throw 0;
	}

	unsigned number_of_rounds = 0;
	in_file >> number_of_rounds;
	if(number_of_rounds == 0)
	{
		throw 0;
	}

	out_file.open(OUTPUT_FILE_PATH, ios_base::binary);
	if(!out_file.is_open())
	{
		throw 0;
	}

	for(unsigned i = 0; i < number_of_rounds; ++i)
	{
		unsigned num_of_snappers, num_of_finger_snaps;
		in_file >> num_of_snappers >> num_of_finger_snaps;

		char* snap_vec = new char[num_of_snappers];
		memset(snap_vec, 0, num_of_snappers);
		
		unsigned point_of_elec = 0;
		for(unsigned j = 0; j < num_of_finger_snaps; ++j)
		{
			if(point_of_elec == num_of_snappers)
			{
				point_of_elec = num_of_snappers - 1;
				snap_vec[point_of_elec] = 0;
			}
			else
			{
				snap_vec[point_of_elec] = 1;
			}
			memset(snap_vec, 0, point_of_elec);
			
			unsigned k;
			for(k = 0; k < num_of_snappers; ++k)
			{
				if(snap_vec[k] == 0)
				{
					break;
				}
			}
			point_of_elec = k;
		}

		out_file << "Case #" << (i + 1) << ": " << (point_of_elec == num_of_snappers ? "ON" : "OFF") << "\n";
	}

	if(!in_file.eof())
	{
		cerr << "Warning - did not reach EOF" << endl;
	}

	in_file.close();
	out_file.close();
}