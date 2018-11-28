#include <fstream>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <map>
using namespace std;

int main(int argc,char* argv[]){
	
	ifstream fp;
	fp.open(argv[1]);
	
	if(fp.is_open()){
		long int num_case = 0;
		long int cur_case = 0;
		ofstream ofp("result.out");
		fp>>num_case;
		
		while(cur_case < num_case){
			long int ans=0;	
			long int A,B;
			string n,m;
			
			fp>>n>>m;
			
			A = atoi(n.c_str());
			B = atoi(m.c_str());
			if(A<0 || B < 0)
				cerr<<"out-of-accuracy"<<endl;
			for(long int i = A; i <=B ; i++){
				string np;
				map<long int,bool> m_check;
				m_check.clear();
				stringstream ss;
				ss.clear();
				ss<<i;
				np = ss.str();
				
				for(long int j = 0 ; j < n.size();j++){
					//cout<<np<<" ---> ";
					np = np[n.size()-1]+np.substr(0,np.size()-1);
					long int num_np = 0;
					num_np = atoi(np.c_str());
					if(i < num_np && num_np<= B && m_check.find(num_np) == m_check.end()){
						m_check[num_np] = true;
						ans++;
						//cout<<ans<<" : "<<A<<"<= "<<i<<" < "<<np<<" <= "<< B<<endl;
					}
					//getchar();
				}	
			}
			//getchar();
			ofp<<"Case #"<<cur_case+1<<": "<<ans<<endl;
			cout<<"Case #"<<cur_case+1<<": "<<ans<<endl;
			cur_case++;
		}
		ofp.close();
		fp.close();
	}
	
	
	
	return 0;
}
