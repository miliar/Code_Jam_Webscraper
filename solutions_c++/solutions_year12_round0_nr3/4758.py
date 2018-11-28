#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

char* rotate_left(char* str, int shift)
{
char* temp = new char;
int j =0;  

     for(int i=0;i<strlen(str);i++)
     {
               
      j=i+shift;
      if(j>=(strlen(str)))
      {
       j = j%(strlen(str));
      }
      temp[i]=str[j];
     }
     temp[strlen(str)]=0;
     
    
return temp;
}

int result(char* str)
{
int prs = 0;

vector<int> myIntVector;
vector<int>::iterator myIntVectorIterator;

char* A = new char;
char* B = new char;
int i=0;
int j=0;

      for(i=0;i<strlen(str);i++)
      {
        if(str[i] == ' ')
        {
          break;
        }
       A[i]=str[i];
      }
      A[i]=0;
      

      for(j=0;j<strlen(str);j++,i++)
      {
       if(str[i]==0)
       {
        break;
       }
       B[j]=str[i];
      }
      B[j]=0;
      
      int a = atoi(A); 
      int b = atoi(B);
      
      
      char* tempa= new char;
      char* tempb= new char;
      
const char* rotated_tempa = new char;
      
      if(a>=1 && b<=1000)
      {
      for(a;a<=b;a++)
      {
       tempa= itoa(a,tempa,10); 
       for(int i=0;i<strlen(tempa);i++)
       {
        rotated_tempa = rotate_left(tempa,i+1);
        
        
        if(rotated_tempa[0]!='0' && atoi(tempa) < atoi(rotated_tempa) && atoi(rotated_tempa) <= b && atoi(rotated_tempa) != atoi(tempa))
        {
          
          myIntVector.push_back(atoi(tempa));
          prs++;
          
          myIntVector.push_back(atoi(rotated_tempa));
          
         
         
        }
       }
      }
      }
      
      int rs = ((int)myIntVector.size()-prs);
       
       
return rs;
}

int main()
{

int lines = 0;
int rslt;
                ifstream in;    
                ofstream out;
                in.open("C-small-attempt1.in");
                out.open("Output.txt");
                
                in>>lines;
char str[256];

in.getline(str, 256);

if(lines<=50 && lines>=1)
{
 for(int i=0;i<lines;i++)
 {
   in.getline(str, 256);
   rslt = result(str);
   out<<"Case #"<<(i+1)<<": "<<rslt<<endl;
 }
}
             in.close();
             out.close();
      
system("pause");
return 0;
}

