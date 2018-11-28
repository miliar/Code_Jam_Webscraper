#include<iostream>
using namespace std;
struct enname{
       char name[101];
       bool isappear;
       };

int main(){
    int test_n;
    cin >> test_n;
    for(int k=0;k<test_n;k++){
    
    int en_num;
    cin >> en_num;
    enname array[100];
    int now=0;
    int change=0;
    for(int i=-1;i<en_num;i++)
    {
            cin.getline(array[i].name,sizeof(array[i].name));
            //cout <<en[i];
            if(i>=0)array[i].isappear=0;
            
     }
    
    
    /* for(int i=0;i<en_num;i++)
    {
           // cin >> en[i];
            cout <<array[i].name<<endl;
     }*/
     int searchn;
     char buffer[101];
     cin >> searchn;
     //cin >> buffer;
     for(int i=0;i<searchn+1;i++)
     {
             cin.getline(buffer,sizeof(buffer));
             //cout << buffer<<" "<<i<<endl;
             for(int j=0;j<en_num;j++)
             {
                     if(array[j].isappear==0 &&strcmp(buffer,array[j].name)==0){array[j].isappear=1;now++;}
             }
             if(now==en_num)
             {    
                  change++;
                  for(int j=0;j<en_num;j++)
                  {
                      if(strcmp(buffer,array[j].name)!=0)array[j].isappear=0;
                  }
                now=1;
             }
            //cout <<change<<endl;
                            
     }       
    cout << "Case #" << k+1 <<": " <<change << endl;
    }     
   //system("pause");
     return 0;
}