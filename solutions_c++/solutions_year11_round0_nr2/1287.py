#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<cstring>
#include<sstream>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
map<string, string> M_c;
set<string> S_d;

int str2int(string s)
	{
		int ret=0;
		for(int i=0;i<s.size();i++) ret=ret*10+(s[i]-'0');
		return ret;
	}

int main()
	{
		int n,x=1;
		string s;
	 	for ( scanf("%d\n",&n) ;n>0 ; n-- )
		{
			M_c.clear();S_d.clear();
			getline(cin,s);
			stringstream ss(s);
			string tmp;
			ss>>tmp;
			int c = str2int(tmp);
			for( int i=0 ; i<c ; i++ ) 
			{
				ss>>tmp;
				string t_1 =  tmp.substr(0,2) ;
				string t_2 =  t_1;
				reverse(t_2.begin(),t_2.end()) ;
				M_c[ t_1  ] = M_c[ t_2 ] = tmp[2];
			}
			
			ss>>tmp;	
			int d = str2int( tmp );
			for( int i=0; i<d; i++ )  
			{
				ss>>tmp;
				S_d.insert( tmp );
				reverse( tmp.begin() , tmp.end() );
				S_d.insert( tmp  );
			}
	
			ss>>tmp;	
			int n = str2int( tmp );
			ss>>tmp;
			string final = tmp;
			vector<string> v;
			string ret_1,ret_2;
		
			/*cout<<"mapping of element \n";
			for(map< string , char > :: iterator it = M_c.begin(); it != M_c.end() ; it++ ) 
			 	cout<<it->first<<" "<<it->second<<endl;

			cout<<"set element \n";
			for( set<string> :: iterator it = S_d.begin();it!=S_d.end();it++) 
				 cout<<*it<<endl;
			*/
			for(int i=0;i<n;i++)
			{
				string tt="";
				tt+=final[i];
				v.push_back( tt );
				//cout<<"inside ";for(int i=0;i<v.size();i++ ) cout<<v[i]<<" ";cout<<endl;
				ret_1=ret_2="";	
				int k = v.size();
				if(k<2) continue;
				ret_1= v[k-2]+v[k-1];
				ret_2= v[k-1]+v[k-2];	
	
				//if ret_1 or ret_2 in v_c then replace it 
				//otherwise if in v_d then pop bot elements 
				
				if(M_c.count( ret_1 )) 
				  {
					//cout<<" ret_1 "<<ret_1<<endl;
					v.pop_back();
					v.pop_back();
					v.push_back(M_c[ret_1]);
					continue;
				  }
				else if(M_c.count(ret_2))
				  {
					//cout<<"ret_2 "<<ret_2<<endl;
					v.pop_back();
					v.pop_back();
					v.push_back(M_c[ret_2]);
					continue;
				  }
				int l=-1;
				for( int j=v.size()-1;j>=0;j-- )
				  {
					string tmp_1="",tmp_2="";
					tmp_1 =  v[j] + v[v.size()-1]  ;
					tmp_2 =  v[v.size()-1] + v[j]  ;
					if(S_d.count(tmp_1) || S_d.count(tmp_2) )
					 {
						//l=max(0,j-1);
						v.clear();
						break;
					}
 				  }
				//if(l==-1) continue;
				//while(v.size()!=l) v.pop_back();
				
			}
			cout<<"Case #"<<x<<": ";
			if(v.size()==0) cout<<"[]"<<endl;
			else if (v.size()==1) cout<<"["<<v[0]<<"]"<<endl;
			else 
			 {
				cout<<"[";
				for(int i=0;i<v.size()-1;i++) cout<<v[i]<<", ";
				cout<<v[v.size()-1]<<"]"<<endl;				

			 }
			x++;
		}
	}

