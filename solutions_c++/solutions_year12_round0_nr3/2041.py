#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int p[]={10,100,1000,10000,100000,1000000,10000000};

string inttostr(int a){
    string res = "";
    while (a>0){
        int c = a%10;
        res = (char)(c+'0')+res;
        a/=10;    
    }    
    return res;
}

int main(void){
    //freopen("B-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    
    int test;
    scanf("%i",&test);
    
    int A,B;    
    for (int z=0;z<test;z++){
        scanf("%i %i",&A,&B);
        int ans = 0;            
        for (int i=A;i<=B;i++){
            for (int k=0;k<7;k++){
                int rig = i%p[k];
                int lef = i/p[k];
                if (lef<=0) break; 
                for (int f = 0;f<7;f++){
                    if (p[f]>lef){
                        int num = rig*p[f]+lef;
                        //if (num>=A){
                            if (num<=B && num>i && num>=A){
                                ans++;
                                //printf("+ (%i,%i)\n",i,num);
                                /*string a = inttostr(i);
                                string b = inttostr(num);
                                bool fal = true;
                                for (int ww = 0;ww<a.size();ww++){
                                    if (a==b) fal = false;
                                    a = a.substr(1, a.size()-1)+a[0];                                            
                                }    
                                if (fal) printf("WRONG!\n");*/
                            }
                            //else break;    
                        //}
                        break;
                    }    
                }
                
                if (lef<=0) break;    
            }                    
        }
        printf("Case #%i: ",z+1);
        printf("%i\n",ans);
    }    
    
    return 0;    
}
