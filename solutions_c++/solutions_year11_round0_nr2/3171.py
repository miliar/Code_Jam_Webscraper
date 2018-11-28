#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;


void solve(int case_number,ofstream* output,char** Combine,int C,char** Oppose,int D,string Characters,int N)
{
	vector<char> myvector;
	bool combined;
	bool cleared;

	for(int i=0;i<N;i++)
	{
		combined = false;
		cleared = false;

		for(int j=0;j<C;j++){

			if( i && ((Combine[j][0] == Characters[i] && Combine[j][1] == myvector.back()) ||
				(Combine[j][1] == Characters[i] && Combine[j][0] == myvector.back()))){
				myvector.pop_back();
				myvector.push_back(Combine[j][2]);
				combined = true;
				break;
			}
			
		}

		for(int j=0;j<D;j++){
			if(myvector.size()<1)break;
			if(combined)break;
			
			for(int k=myvector.size()-1;k>=0;k--){
				if( (Characters[i]==Oppose[j][0] && myvector[k]==Oppose[j][1]) ||
					(Characters[i]==Oppose[j][1] && myvector[k]==Oppose[j][0]) ){
					cleared = true;
					myvector.clear();
					break;
				}
			
			
			}
		}	
		if(!combined && !cleared){
			myvector.push_back(Characters[i]);
		}	
	}
	
	*output << "Case #" << case_number << ": [";
	for(int i=0;i<myvector.size();i++){
		*output << myvector[i];
		if(i!=myvector.size()-1) *output << ", ";
	}
	*output << "]" << endl;
}

int main()
{
	ifstream input("B-large.IN");
	ofstream output("output.txt");
	int T;
	int C;
	int D;
	int N;
	input >> T;
	for(int i=0;i<T;i++)
	{
		input >> C;
		char** Combine = new char*[C];	

		for(int j=0;j<C;j++){
			Combine[j] = new char[3];
			input >> Combine[j];
		}
		
		input >> D;
		char** Oppose = new char*[D];
		for(int j=0;j<D;j++){
			Oppose[j] = new char[2];
			input >> Oppose[j];
		}		

		input >> N;
		string Characters;
		input >> Characters;

		solve(i+1,&output,Combine,C,Oppose,D,Characters,N);
	}
	
	return 0;
}
