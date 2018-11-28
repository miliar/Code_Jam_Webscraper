#include <iostream>
#include <fstream>
#include <list>
#include <string>

using namespace std;

int main()
{
	int T, C, D, N;
	string temp;
	string input;
	string output;
	list<string> combinations;
	list<string> repulsions;
	ifstream file("B-small-attempt0.in");
	ofstream ofile("B-small-attempt0.out");
	file>>T;
	for(int i =0;i<T; i++){
		file >> C;
		output.clear();
		combinations.clear();
		repulsions.clear();
		for(int j =0;j<C; j++){
			file >> temp;
			combinations.push_back(temp);
		}
		file >> D;
		for(int k =0;k<D; k++){
			file >> temp;
			repulsions.push_back(temp);
		}
		file >> N;
		file >> input;

		for (string::iterator sit = input.begin(); sit !=input.end(); ++sit)
		{
			bool combo = false;
			if (sit == input.begin()){
				output.append(1,*sit);
				continue;
			}
			list<string>::iterator comit;
			char last = output[output.size()-1];
			for (comit = combinations.begin(); comit!=combinations.end();++comit)
			{
				if((*sit==(*comit)[0] && last==(*comit)[1]) || (*sit==(*comit)[1] && last==(*comit)[0])){
					output[output.size()-1]=(*comit)[2];
					combo = true;
					break;
				}
			}
			if(!combo)
				output.append(1,*sit);

			list<string>::iterator repit;

			for (repit = repulsions.begin(); repit!=repulsions.end();++repit)
			{
				if((output.find((*repit)[0])!=string::npos) && (output.find((*repit)[1])!=string::npos))
					output.clear();
				break;

			}
		}


		ofile << "Case #" << i+1 << ": ["; 
		for (string::iterator outit = output.begin();outit!=output.end(); ++outit){
			ofile<< *outit;
			if (outit!=(output.end()-1))
				ofile << ", ";
		}
		ofile << "]" << endl;

	}
	file.close();
	ofile.close();

}