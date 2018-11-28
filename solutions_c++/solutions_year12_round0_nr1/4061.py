#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main (int argc, char * const argv[]) {
	string line;
	//ifstream myfile ("test_input.txt");
	ifstream myfile ("test_input.txt");
	//char in[27]  = {' ','y','n','f','i','c','w','l','b','k','u','o','m','l','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	//char out[27] = {' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	string ins  = " ynficwlbkuomxsevzpdrjgthaq";
	string outs = " abcdefghijklmnopqrstuvwxyz";
	
	int n,i,j;
	if (myfile.is_open())
	{
		getline (myfile,line);
		stringstream strStream(line);
		strStream>>n;
		for (i=1;i<=n;i++)
		{
			getline (myfile,line);
			
			cout<<"Case #"<<i<<": ";
			for(j=0;j<line.size();j++){
				cout<<outs.at(ins.find(line.at(j)));
			}
			cout<<endl;
			//cout << line << endl;
		}
		myfile.close();	
	}
	else cout << "Unable to open file"; 
    return 0;
}