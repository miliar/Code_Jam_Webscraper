#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

void swap(long int *a, long int *b){
	long int temp;
	temp=*a;
	*b=*a;
	*a=temp;
}

int sort(int a[],int n){
    for(int i=0;i<n-1;i++)
            for(int j=i+1;j<n;j++)
                    if(a[i]<a[j])
                                 swap(a[i],a[j]);
}
long int func(int f[],int p,int k,int l){
    long int ans=0,m=1;
    for(int i=0;i<l;i++){
            m=(int)(i/k)+1;
            ans+=m*f[i];
    }
    return ans;
}
        
int main(){
    int n,p,k,l,*f;
long int ans;
    ifstream in("A-small1.in");
	ofstream out("A-small.out"); 
	in>>n;
	for(int q=1;q<=n;q++){
            in>>p>>k>>l;
            f= new int[l];
            for(int i=0;i<l;i++)
                    in>>f[i];
            if(p*k>=l){
                sort(f,l);
                ans=func(f,p,k,l);
                out<<"Case #"<<q<<": "<<ans<<endl;
            }
            else
                out<<"Case #"<<q<<": Impossible "<<endl;    
    }
    in.close();
    out.close();
}
