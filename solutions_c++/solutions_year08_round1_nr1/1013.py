#include<iostream>
#include<algorithm>
#include<sstream>
#include<fstream>
#include<vector>
#include<string>
#include<list>
#include<map>


using namespace std;



int main()
{
    int T,N;
    
   
    
   
	FILE* in;
    in=fopen("input.txt","r");	
    fstream out("output.out",ios::out);

	fscanf(in,"%d",&T);  
    cout<<T<<endl;

for(int c=0;c<T;++c)
{
	fscanf(in,"%d",&N);  
    cout<<N<<endl;
 
    vector<int>a(N);
    
    for(int i=0;i<N;++i)
    fscanf(in,"%d",&a[i]);  
    
       
    vector<int>b(N);
    for(int i=0;i<N;++i)    
    fscanf(in,"%d",&b[i]);  

   sort(a.begin(),a.end());
   sort(b.begin(),b.end());
   reverse(b.begin(),b.end());
   
   int sum=0;
   for(int i=0;i<N;++i)
   sum+=(a[i]*b[i]);		
		 	
   out<<"Case #"<<c+1<<": "<<sum<<endl;
	
}
	fclose(in);
	out.close();
	system("pause");
	return 0;
}
