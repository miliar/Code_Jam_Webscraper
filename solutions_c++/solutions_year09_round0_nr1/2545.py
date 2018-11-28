
#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<cstdlib>
#include<cstring>
using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vb> vvb;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define sz(c) (int)c.size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define inc(i,n) for(int i=0;i<n;i++)
#define dec(i,n) for(int i=n-1;i>=0;i--)
int main(){
			int len,n,q;
				cin>>len>>n>>q;
					vector<string> v(n);
						for(int i=0;i<n;i++){
									cin>>v[i];
										}
							int count=0;
								for(int z=0;z<q;z++){
											string s;
													cin>>s;
															count =0;
																	for(int i=0;i<n;i++){
																					int index=0;
																								for(int p=0;p<s.size();p++){
																													bool flag =0;
																																	if(s[p]=='('){
																																							while(s[p]!=')'){
																																														if(s[p]==v[i][index]){
																																																						flag=1;
																																																													
																																																												}
																																																				p++;
																																																									}
																																											}
																																					else{
																																											if(s[p]==v[i][index])
																																																		flag =1;
																																															}
																																									if(flag)
																																															index++;
																																													else
																																																			break;
																																																}
																											if(index==len){
																																++count;
																																			}
																													}
																			printf("Case #%d: %d\n",z+1,count);
																				}
	}

