#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<map>
#include<cstdlib>
#include <queue>
#include <fstream>

using namespace std;

vector<int> fun(int num)
{
    vector<int> vec;
    int rem;
    while(num/10!=0){
        rem=num%10;
        num/=10;
        vec.push_back(rem);
    }

    vec.push_back(num);

    return vec;
}

void swap(string &s,int a,int b)
{
    char c;
    c=s[a];
    s[a]=s[b];
    s[b]=c;
    return;
}

int main()
{
    ifstream ifile("data.txt");
    ofstream ofile("data1.txt");

    int n;
    ifile >> n;

    vector<int> vec;
    string s;
    int flag=0,flag2=0;
    int k=0;

    for(int j=0;j<n;j++){
        vec.clear();
        
            s.clear();
            ifile >> s;
        


        for(int i=s.size()-2;i>=0;i--){
            flag=0;
            for(k=s.size()-1;k>i;k--){
                if(s[k]>s[i]){
                    if(flag==0){
                        flag=1;
                        if(s[k-1]==s[k]){
                            continue;
                        }else{
                            break;
                        }
                    }else if(flag>0){
                        if(s[k-1]==s[k]){
                            continue;
                        }else{
                            break;
                        }
                    }
                }
                if(flag>0)break;
            }
            
            
            if(flag>0){
                swap(s,k,i);
                for(int k=i+1;k<s.size();k++){
                    vec.push_back((int)(s[k]-48));
                }

                sort(vec.begin(),vec.end());
                
                for(int k=i+1;k<s.size();k++){
                    s[k]=(char)(vec[k-(i+1)]+48);
                }
                ofile <<"Case #"<<j+1<<": " << s << endl;
                
                break;
            }
            
        }
        if(flag==0){
            s.push_back('0');
            vec.clear();
            for(int k=0;k<s.size();k++){
                    vec.push_back((int)(s[k]-48));
            }

            sort(vec.begin(),vec.end());
           

            int min;
            int index;
            for(int k=0;k<s.size();k++){
                 if((char)(vec[k])!=0){
                    min=(char)(vec[k]+48);
                    index=k;
                    break;
                }
            }
            
            string temp;
            temp.push_back(min);
            for(int k=0;k<vec.size();k++){
                if(k==index)continue;
                temp.push_back((char)(vec[k]+48));
            }
                ofile <<"Case #"<<j+1<<": " << temp << endl;


        }
        ifile.clear();
            ofile.clear();
        
    }
    //system("pause");
    return 0;
}
