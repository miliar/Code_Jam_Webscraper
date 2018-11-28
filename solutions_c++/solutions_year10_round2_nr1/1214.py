#include <iostream>
using namespace std;



    string dir[10000];
    int dirlen=0;

    int finddir(string s){
        for (int i=0;i<dirlen;i++)
            if(s==dir[i])
            return i;
        return -1;
        }


main()
{


      
      int t,n,m;
      scanf("%d\n",&t);
      for (int i=0;i!=t; i++){
          scanf("%d%d\n",&n,&m);
          dirlen=0;
          for (int j=0;j!=n;j++){
              string s;
              getline(cin,s);
              s+='/';
              string tmp="";

              for (int k=1;k!=s.length();k++){
                  if (s[k]=='/'){
                     int pos = finddir(tmp);
                     if (pos == -1){
                        dir[dirlen++]=tmp;
                        }
                     }
                  tmp+=s[k];
              }
          } 
           
          int count =0;
          for (int j=0; j!=m; j++){
             string s;
              getline(cin,s);
              s+='/';
              string tmp="";

              for (int k=1;k!=s.length();k++){
                  if (s[k]=='/'){
                     int pos = finddir(tmp);
                     if (pos == -1){
                        dir[dirlen++]=tmp;
                        count ++;
                        }
                     }
                  tmp+=s[k];
              }
          }
          

      cout <<"Case #"<<i+1<<": "<<count << endl;
      
      }

}
