#include <iostream.h>
#include <map>
#include <string>
using namespace std;

int main(){
	string w;
	int N;
	cin >> N;
	int result[N];
	for(int p=0;p<N;p++){

	int n_engines;
	map <string,int> M;
	int i;
	cin >> n_engines;


	getline(cin,w);
	
	for(i=0;i<n_engines;i++){
		string a;
		getline(cin,a);
		M[a]=0;
	}

		int queries;
		int switches=0;
		int found=0;
		string previous_engine="";
		//string previous="";
		cin >> queries;
		
		getline(cin,w);
		
	for(int k=0;k<queries;k++){
			string a;
			getline(cin,a);
			if ((M[a]==0)&&(a!=previous_engine)) found++;
			else;
			(M[a])++;
			/*if ((found==(n_engines-1))) {
				switches++;
				previous_engine = previous;
				found=0;
				for(map<string,int>::iterator it = M.begin(); it != M.end(); ++it)
    				{
					it->second=0;
				    }
				(M[a])++;
				}*/
			if ((found==(n_engines-1))&&(previous_engine!="")) {
				//cout << "\nm    " << a << "\n";
				switches++;
				previous_engine = a;
				found=0;
				
				for(map<string,int>::iterator it = M.begin(); it != M.end(); ++it)
                                {
                                        it->second=0;
                                    }
                                    
                                    
				}
			
			else if ((found==n_engines)&&(previous_engine=="")){
				//cout << "\nr    " << a << "\n";
				switches++;
				previous_engine = a;
				found=0;
				
				for(map<string,int>::iterator it = M.begin(); it != M.end(); ++it)
                                {
                                        it->second=0;
                                    }
                                    
                                    
				}
			else;
			//previous = a;
			}
	
	result[p] = switches;

	}


	for(int g=0;g<N;g++){
		cout << "Case #" << (g+1) << ": " << result[g] << "\n";
	}

	return 0;
}
