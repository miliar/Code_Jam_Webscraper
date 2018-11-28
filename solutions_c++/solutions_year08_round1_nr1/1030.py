#include<iostream>
#include<fstream>
using namespace std;

void rev(int b[],int n){
     int temp;
     for(int i=0;i<n/2;i++){
             temp=b[n-i-1];
             b[n-1-i]=b[i];
             b[i]=temp;
     }
}

void swap(int *a, int *b){
	int temp;
	temp=*a;
	*b=*a;
	*a=temp;
}

void sorta(int x[],int n){
     for(int i=0;i<n-1;i++)
             for(int j=i+1;j<n;j++)
                     if(x[i]>x[j])
                                  swap(x[i],x[j]);
}

int mult(int a[],int b[],int n){
    int ans=0;
    for(int i=0;i<n;i++)
            ans+=a[i]*b[i];
    return ans;
}

int main(){
    int n,T,ans;
    int *a,*b;	
	ifstream in("A-small.in");
	ofstream out("A-small.out"); 
	in>>T;
	for(int l=1;l<=T;l++){
            in>>n;
            a= new int[n];
            b=new int[n];
            for(int i=0;i<n;i++)
                    in>>a[i];
            for(int i=0;i<n;i++)
                    in>>b[i];
            sorta(a,n);
            sorta(b,n);
            rev(b,n);
            ans=mult(a,b,n);
            out<<"Case #"<<l<<": "<<ans<<endl;
            delete [] a;
            delete [] b;
            }
     out.close();
     in.close();
}
