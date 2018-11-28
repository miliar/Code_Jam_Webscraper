#include <iostream>
#include <string>
  #include<map>
  
  using namespace std;

map <string, int> map1 ;

int n;
int ns;
int nq;

int check[101];
int counter = 0 ;
int answer = 0;
int main()
{
   cin>>n;
   int i;
   string temp;
   
   for (i = 0 ; i<n;i++)
   {
     map1.clear();
     cin>>ns;
     getline(cin, temp);
     counter = 0;
     answer = 0;
           for (int x = 0 ; x<ns;x++)
            check [x] = 0;
           
     for (int j = 0; j<ns;j++)
     {
       getline(cin, temp);
       map1[temp]=j;
     }
     
     cin >>nq;
     getline(cin, temp);
     for (int j = 0; j<nq;j++)
     {
        getline(cin, temp);
        
        if (check[ map1[temp] ]==0)
        {
          check[ map1[temp] ] = 1;
          counter ++;
        }
        if (counter == ns)
        {
          answer ++;
          counter =1;
          for (int x = 0 ; x<ns;x++)
            check [x] = 0;
          check [ map1[temp] ]= 1;
        }
     }
     cout<<"Case #"<<i+1<<": "<<answer<<endl;
   }
   return 0;
}
