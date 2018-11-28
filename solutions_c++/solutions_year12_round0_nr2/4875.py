#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int t;
	int cas=1;
	cin>>t;
	while(t--){
		int n,s2,p;
		cin>>n>>s2>>p;
		int t[n];
		int s[n][2][4];
		int s1[n];
		int sup=0, unsup=0;
		vector<int> only;
		vector<int> both;
		vector<int> only1;
		vector<int> to_use;
		int count1=0;
		bool main_flag=true;
		for(int i=0; i<n; ++i){
			cin>>t[i];
		}
		
		cout<<"Case #"<<cas<<": ";
		cas++;

		for(int i=0; i<n; ++i){
			s[i][0][0]=0;
			s[i][1][0]=0;
			s1[i]=0;
			if((t[i]-2)>=0 && (t[i]-2)%3==0){
				s[i][0][0]=1;
				s[i][0][1]=1;
				s[i][1][0]=1;
				s[i][1][3]=1;
			}else{
				s[i][0][1]=0;
				s[i][1][3]=0;
			}
			if((t[i]-3)>=0 && (t[i]-3)%3==0){
				s[i][0][0]=1;
				s[i][0][2]=1;
			}else{
				s[i][0][2]=0;
			}
			if((t[i]-4)>=0 && (t[i]-4)%3==0){
				s[i][0][0]=1;
				s[i][0][3]=1;
			}else{
				s[i][0][3]=0;
			}
			if((t[i])>=0 && (t[i])%3==0){
				s[i][1][0]=1;
				s[i][1][1]=1;
			}else{
				s[i][1][1]=0;
			}
			if((t[i]-1)>=0 && (t[i]-1)%3==0){
				s[i][1][0]=1;
				s[i][1][2]=1;
			}else{
				s[i][1][2]=0;
			}
		}

		int sz,sz1,sz2;
		for(int i=0; i<n; ++i){
			if(t[i]==0 || t[i]==1){
				only1.push_back(i);
			}else{
				both.push_back(i);
			}
		}

		sz=only.size();
		sz1=only1.size();
		sz2=both.size();
		sup=sz2+sz;
		unsup=sz2+sz1;
		int count=0;
		vector<int> both1;
		vector<int> only2;
		int br;

		/*cout<<"\n*****\n";
		cout<<"only:\n";
		for(int i=0; i<sz; ++i){
			cout<<only[i]<<endl;
		}
		cout<<"only1:\n";
		for(int i=0; i<sz1; ++i){
			cout<<only1[i]<<endl;
		}
		cout<<"both:\n";
		for(int i=0; i<sz2; ++i){
			cout<<both[i]<<endl;
		}
		cout<<"\n****\n";*/

		if(sup<s2){
			cout<<"0\n";
			main_flag=false;
		}else{
			if(sz<s2){
				for(int i=0; i<sz; ++i){
					to_use.push_back(only[i]);
					s1[only[i]]=1;
				}
				int remain=s2-to_use.size();
				for(int i=0; i<sz2; ++i){
					bool flag1=false,flag2=false;
					if(s[both[i]][0][1]==1){
						int a=(t[both[i]]-2)/3;
						if(a>=p || a+2>=p){
							flag1=true;
						}
					}else if(s[both[i]][0][2]==1){
						int a=(t[both[i]]-3)/3;
						if(a>=p || a+1>=p || a+2>=p){
							flag1=true;
						}
					}else if(s[both[i]][0][3]==1){
						int a=(t[both[i]]-4)/3;
						if(a>=p || a+2>=p){
							flag1=true;
						}
					}
					if(s[both[i]][1][1]==1){
						int a=(t[both[i]])/3;
						if(a>=p){
							flag2=true;
						}
					}else if(s[both[i]][1][2]==1){
						int a=(t[both[i]]-1)/3;
						if(a>=p || a+1>=p){
							flag2=true;
						}
					}else if(s[both[i]][1][3]==1){
						int a=(t[both[i]]-2)/3;
						if(a>=p || a+1>=p){
							flag2=true;
						}
					}
					if(flag1 && flag2){
						both1.push_back(both[i]);
					}else if(flag1){
						only2.push_back(both[i]);
					}
				}
				int sz3=only2.size();
				br=to_use.size();
				if(sz3<remain){
						for(int i=0; i<sz3; ++i){
							to_use.push_back(only2[i]);
							s1[only2[i]]=1;
						}
						remain=remain-sz3;
						int sz4=both1.size();
						//if(remain<=sz4){
							for(int i=0; i<remain && i<sz4; ++i){
								to_use.push_back(both1[i]);
								s1[both1[i]]=1;
							}
						/*}else{
							cout<<"0\n";
							main_flag=false;
						}*/
				}else{
					for(int i=0; i<remain; ++i){
						to_use.push_back(only2[i]);
						s1[only2[i]]=1;
					}
				}
			}else{
				for(int i=0; i<s2; ++i){
					to_use.push_back(only[i]);
					s1[only[i]]=1;
				}
				br=to_use.size();
			}

			for(int i=0; i<br; ++i){
				bool flag1=false;
				if(s[to_use[i]][0][1]==1){
					int a=(t[to_use[i]]-2)/3;
					if(a>=p || a+2>=p){
						flag1=true;
					}
				}else if(s[to_use[i]][0][2]==1){
					int a=(t[to_use[i]]-3)/3;
					if(a>=p || a+1>=p || a+2>=p){
						flag1=true;
					}
				}else if(s[to_use[i]][0][3]==1){
					int a=(t[to_use[i]]-4)/3;
					if(a>=p || a+2>=p){
						flag1=true;
					}
				}
				if(flag1){
					count1++;
				}
			}
			int sz5=to_use.size();
			count1+=sz5-br;

			for(int i=0; i<n; ++i){
				if(s1[i]==0){
					bool flag1=false;
					if(s[i][1][1]==1){
						int a=(t[i])/3;
						if(a>=p){
							flag1=true;
						}
					}else if(s[i][1][2]==1){
						int a=(t[i]-1)/3;
						if(a>=p || a+1>=p){
							flag1=true;
						}
					}else if(s[i][1][3]==1){
						int a=(t[i]-2)/3;
						if(a>=p || a+1>=p){
							flag1=true;
						}
					}
					if(flag1){
						count1++;
					}
				}
			}
			if(main_flag){
				cout<<count1<<endl;
			}
		}
	}
	return 0;
}
