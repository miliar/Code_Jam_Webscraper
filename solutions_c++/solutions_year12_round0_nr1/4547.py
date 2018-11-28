#include<iostream>
#include<string>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
    int t= 0;
    char arr[26];
    arr[0] = 'y';
    arr[1] = 'h';
    arr[2] = 'e';
    arr[3] = 's';
    arr[4] = 'o';
    arr[5] = 'c';
    arr[6] = 'v';
    arr[7] = 'x';
    arr[8] = 'd';
    arr[9] = 'u';
    arr[10] = 'i';
    arr[11] = 'g';
    arr[12] = 'l';
    arr[13] = 'b';
    arr[14] = 'k';
    arr[15] = 'r';
    arr[16] = 'z';
    arr[17] = 't';
    arr[18] = 'n';
    arr[19] = 'w';
    arr[20] = 'j';
    arr[21] = 'p';
    arr[22] = 'f';
    arr[23] = 'm';
    arr[24] = 'a';
    arr[25] = 'q';
//    cin>>t;
    string s;    
    //cout<<"xh";
    ifstream myfile;
    myfile.open("A-small-attempt1.in"); 
    ofstream ofile;
    ofile.open("output.txt");
    int count = 0;
    int h= 0;
  //  cout<<"qwe";
  if (myfile.is_open())
  {
    while ( myfile.good() && !myfile.eof() )
    {
          h++;
      getline(myfile,s);
      if(count == 0){
          for(int k = s.size()-1;k>=0;k--){
                  t = t + (s[k]-48)*pow(10,s.size()-k-1);
          }
          //cout<<t;
          count = 1;
          continue;
      }
      if(h >t+1 )break;
//      for(int j=0;j<t;j++){
            for(int i=0;i<s.size();i++){
                    if(s[i]-97 >=0 && s[i]-97 <=25 )
                    s[i] = arr[s[i]-97];
            }
            if (ofile.is_open()){
                     ofile <<"Case #"<<h-1<<": "<<s<<endl;
            } else cout<<"cccc";
  //    }
         
//      cout << line << endl;
}

}else cout<<"ABCDEFGHIJKL";    
 //system("pause");
    return 0;
}
    
