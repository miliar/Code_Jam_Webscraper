#include <cstdlib>
#include <iostream>
#include <fstream>


using namespace std;

int pow(int base, int p)
{
    int result=1;
    for (int i=0; i<p; i++)
        result=result*base;
    return result;  
}

bool check(int a[], int size, int target){
     for ( int i=0;i<size; i++)
         if (a[i]==target)
            return true;
     return false;
}

int main(int argc, char *argv[])
{
    ifstream file;
    ofstream write;
    write.open("output.txt");
    
    file.open("C-large.in");
    
    string numInput;
    getline(file,numInput);
    int num=1;
    
    while(!file.eof())
    {          
         string a,b;
         int result=0;
         file>>a>>b;
         int digit=a.size();
         int A=atoi(a.c_str());
         int B=atoi(b.c_str());
         for ( int n=A;n<=B; n++){
             int temp[digit];
             int count=0;
             for ( int k=1; k<digit; k++)
             {
                 int div = pow(10,k);
                 int last = n%div;
                 int first = n/div;
                 int m = last*pow(10,digit-k)+first;
                 if (m > n && m <=B && !check(temp,count,m) ) {
                    temp[count]=m;
                    count++;
                    result++;
                 }
             }    
         }
         write<<"Case #"<<num<<": "<<result<<endl;
         num++;
    }
    file.close();
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
