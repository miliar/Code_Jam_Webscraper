#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

class triple{
	public:
		
		triple();
		triple(int s,int o,int r):m_score(s),m_over3(o),m_rem(r){
		};
		void set(int s,int o,int r){
			m_score	=s;
			m_over3	=o;
			m_rem	=r;
		};
		int get_score(){
			return m_score;
		};
		int get_over3(){
			return m_over3;
		};
		int get_rem(){
			return m_rem;
		};
		
	private:
		int m_score;
		int m_over3;
		int m_rem;
};

int main(int argc, char* argv[]){
	
	ifstream fp;
	ofstream ofp("result.out");
	fp.open(argv[1]);
	
	if(fp.is_open()){
		
		int case_num = 0,cur_case = 0;
		
		fp>>case_num;
		
		while(cur_case<case_num){
			
			int googlers = 0;
			int surprings = 0;
			int p = 0;
			int ans =0;
			vector<triple> v;
			v.clear();			
			fp>>googlers>>surprings>>p;
			//cout<<"check1"<<endl;
			//getchar();
			for(int i = 0 ; i < googlers; i++){
				int tmp;
				fp>>tmp;
				triple t_triple(tmp,tmp/3,tmp%3);
				v.push_back(t_triple);
			}
			//==========
			//cout<<"check2"<<endl;
			//getchar();
			for(int i = 0 ; i < v.size();i++){
				//cout<<v[i].get_score()<<" "<<v[i].get_over3()<<" "<<v[i].get_rem()<<endl;
				if(v[i].get_over3()>=p){
					ans++;
				}
				else if((v[i].get_over3()) == p-1){
					if(v[i].get_rem() == 1 || v[i].get_rem()==2) ans++;
					else if(surprings>0 && v[i].get_rem() ==0 && v[i].get_over3() >= 1){
						ans++;
						surprings--;
					}
					
				}
				else if(surprings>0 && v[i].get_over3() == p-2 && v[i].get_rem() ==2){
						ans++;
						surprings--;
					
				}
			}
			//still many surprings constraint
			//cout<<"check3"<<endl;
			//getchar();
			if(surprings>0){
				cout<<v.size()<<endl;
				for(int i = 0 ; i < v.size() && surprings > 0;i++){
					if((v[i].get_over3() >= p &&v[i].get_over3() >= 1) || (v[i].get_rem() == p-1 && v[i].get_rem()==2)){
						surprings--;
					}
					//cout<<"check "<<i<<endl;
					//getchar();
				}
				
			}	
			
			//=============
			ofp<<"Case #"<<cur_case+1<<": "<<ans<<endl;
			cout<<"Case #"<<cur_case+1<<": "<<ans<<endl;
			cur_case++;
			//getchar();
		}
		
		ofp.close();
		fp.close();
	}
	
	
	return 0;
}
