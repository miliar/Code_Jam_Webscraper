/*
	evilrus
	Uladzimir Karneyenka
	Snapper Chain

	Microsoft Visual Studio 2008 Pro

*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

#define ERR_NO_INPUT 1
#define ERR_CANT_OPEN_INPUT 2
#define ERR_CANT_OPEN_OUTPUT 3
#define ERR_NO_MEM 4

int main(int argc, char* argv[])
{
	char buffer[1024];

	if(argc < 2)
	{
		cout << "input file name is not provided" << endl;
		return ERR_NO_INPUT;
	}

	string ifname(argv[1]);
	string ofname("");

	if(argc == 2)
	{
		int file_extension_pos = ifname.find_last_of(".");
		if( file_extension_pos == string::npos )
			ofname = ifname;
		else
			ofname = ifname.substr( 0, file_extension_pos );
		ofname += ".out";
	}
	else
		ofname = argv[2];
	
	cout << "input file: " << ifname << endl;
	cout << "output file: " << ofname << endl;

	ifstream input_file(ifname.c_str());
	if( input_file.bad() || !input_file.is_open() )
	{
		cout << "failed opening the input file" << endl;
		return ERR_CANT_OPEN_INPUT; 
	}
	ofstream output_file(ofname.c_str());
	if( output_file.bad() || !output_file.is_open() )
	{
		cout << "failed opening the output file" << endl;
		return ERR_CANT_OPEN_OUTPUT;
	}

	int N = 0;
	int K = 0;
	int T = 0;
	
	
	input_file >> T; // get T
	//cout << "Number of cases: " << T << endl;

	input_file.getline(buffer, 1024); // skip newline char from the first line

	for(int case_count = 1; case_count <= T; case_count++ )
	{
		cout << "\rCase #" << case_count;

		input_file.getline(buffer, 1024);
		//cout << "Case# " << case_count << "intput: " << buffer << endl;

		istringstream istream(buffer);

		istream >> N >> K;
		//cout << "N=" << N << "; K=" << K << endl;

		bool* snappers = new (nothrow) bool[N];
		if(snappers == 0)
		{
			cout << "Failed to alloc memory." << endl;
			return ERR_NO_MEM;
		}

		for(int j = 0; j < N; j++)
			snappers[j] = false;

		bool prev_snapper_old_val = false;
		for(int i = 0; i < K; i++)
		{
			prev_snapper_old_val = snappers[0];
			snappers[0] = !snappers[0]; // the first snapper always toggles
			for(int j = 1; j < N; j++)
				if(prev_snapper_old_val)
				{
					prev_snapper_old_val = snappers[j];
					snappers[j] = !snappers[j];
				}
				else
					j = N; // breaking out from the nested for-loop
		}

		string light_bulb("ON");
		for(int j = 0; j < N; j++)
			if( snappers[j] == false )
			{
				light_bulb = "OFF";
				break;
			}

		output_file << "Case #" << case_count << ": " << light_bulb << endl ;

		delete[]snappers;
	}

	cout << endl << "Done" << endl;
	
	return 0;
}