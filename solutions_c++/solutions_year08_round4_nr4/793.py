/*Author Gaurav Agarwal */
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
#include<complex>
using namespace std;

#define Debug 0
#define LET(x,a)        __typeof(a) x(a)
#define EACH(it,v)      IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)      for(int i=(int)(a) ; i < (int)(b);++i)
#define FORD(i,a,b)     for(int i=(a);i>=(b);--i)
#define REP(i,n)        FOR(i,0,n)
#define SZ              size()
#define PB              push_back
#define PF              push_front
#define PRINT(x)        cout<<#x<<" = "<<x<<endl
#define PRINTI(x,n)     REP(i,n) cout<<(x)[i]<<" ";cout<<endl
#define PRINTIJ(x,m,n)  for(__typeof(m) i=0;i<m;++i,cout<<"\n") REP(j,n) cout<<(x)[i][j]<<" "
#define PRESENT(c,x)    ((c).find(x) != (c).end())
#define CPRESENT(c,x)   (find(c.begin(),c.end(),x) != (c).end())
#define EPS             1e-9
int main(){
	        int t;cin>>t;
		        FOR(cas,1,t+1)
				        {
						                int k;
								                scanf("%d\nnii",&k);
										                char a[10000],tmp[20000];
												                gets(a);
														                int l=strlen(a),ans=INF;
																                string ss[10];
																		                ss[0]="0";
																				                ss[1]="01";
																						                ss[2]="012";
																								                ss[3]="0123";
																										                ss[4]="01234";
																												                string s="0123456";
																														//              for(int i=0;i<k;++i){
																														//                      ss=(char)(i-'0');
																														//                      s+=ss;
																														//              }
																														                s=ss[k-1];
																																                                do
																																					                                {
																																										                                        //cout<<s<<endl;
																																										                                        for(int i=0;i<l;++i)
																																																                                        {
																																																						                                                int pp=k*(i/k),rm=i%k;
																																																												                                                //cout<<pp<<" "<<rm<<endl;
																																																												                                                tmp[i]=a[pp+s[rm]-'0'];
																																																																		                                        }
																																															                                        int tt=0;
																																																				                                        //cout<<tmp<<endl;
																																																				                                        for(int i=0;i<l;)
																																																										                                        {
																																																																                                                int uu=i;
																																																																						                                                while(i<l&&tmp[i]==tmp[uu])i++;
																																																																												                                                tt++;

																																																																																		                                        }
																																																									                                //      cout<<tt<<" "<<tmp<<endl;
																																																									                                        ans<?=tt;

																																																														                                }while(next_permutation(s.begin(),s.end()));
																																				cout<<"Case :"<<cas<<": "<<ans<<endl;




																																				        }
			        return 0;
}

