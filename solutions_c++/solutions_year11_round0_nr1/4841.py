#include<fstream>
#include<iostream>
#include<vector>
#include<cstdlib>
using namespace std;

int main(){
		ifstream fin("a.in");
		ofstream fout("a.out");
        int n;
        fin>>n;
        for(int c=1;c<=n;c++){
                int res=0;
                int t;
                fin>>t;
                int p1=1,p2=1;
				int t1=0,t2=0;
                char cur=' ';
                int tmp=0;
                for(int j=0;j<t;j++){
                        char r;int b;
                        fin>>r;
                        fin>>b;
/*                      if(r=='O'){
                                if(t1>0){t1-=abs(b-p1)+1;}
                                if(t1<0){t2=-t1;res+=t1=0;}
                        }
                        else{
                                t2-=abs(b-p2)+1;
                                if(t2<0){t1=-t2;t2=0;}
                        }
*/                      if(r==cur){
                                if(r=='O'){
                                        tmp+=abs(p1-b)+1;
                                        res+=abs(p1-b)+1;
                                        p1=b;
                                }
                                else {
                                        tmp+=abs(p2-b)+1;
                                        res+=abs(p2-b)+1;
                                        p2=b;
                                }
                        }
                        else{
                                int time=((r=='O')?abs(p1-b):abs(p2-b));
                                if(tmp>=time){tmp=0;}
                                else{
                                        res+= time-tmp;
                                        tmp = time-tmp;
                                }
                                tmp++;res++;
                                if(r=='O')p1=b;
                                else p2=b;

                                cur=r;
                        }
                        //res = t1+t2;
                }
                fout<<"Case #"<<c<<": "<<res<<endl;
        }
}