#include<iostream>
using namespace std;

int main()
{
     freopen ("A-small-attempt1.in","r",stdin);
    freopen ("myfile.txt","w",stdout);
    int map [28];
    string starr1[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string starr2[3] = {"our language is impossible to understand"
    , "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
    };
     
     
    for(int i=0;i<3;i++)
    {
            string str1 = starr1[i];
            string str2 = starr2[i];
             
            for(int j=0;j<str1.length();j++)
            {
                 
                    if(str1[j]>='a' && str1[j]<='z')
                      map[str1[j] - 'a'] = str2[j];
            }
    }
    map['q'-'a'] = 'z';
    map['e'-'a'] = 'o';
    map['y'-'a'] = 'a';
    map['z'-'a'] = 'q';
   // for(int i=0;i<28;i++)
  //  {
  //         cout<<i<<" "<<(char)(i+'a')<<" "<<(char)map[i]<<endl;
//   }
    int T;
    cin>>T;
    string help;
    getline(cin,help);
    for(int TN = 1; TN<= T;TN++)
    {
             
            string strin,strout;
    
            getline(cin,strin);
            for(int j=0;j<strin.length();j++)
            {
                    if(!(strin[j]>='a' && strin[j]<='z'))
                                strout+=(char) strin[j];
                    else
                       strout+= (char) map[strin[j] - 'a'];
            }
            cout<<"Case #"<<TN<<": "<<strout<<endl;
    }
   
    return 0;
}
