  #include "iostream.h"
  unsigned long int T,N,L, H;
  
int hcf_function(int a,int b)
{int c;
    while(1)
    {
  	c = a%b;
  	if(c==0)
  	  return b;
  	a = b;
  	b = c;
    }
  }
  
int lcm_function(int m,int n)
{
int lcm;
if (m%n==0 && n!=1)
return n;

if(n%m==0&& m!=1)
return m;

lcm=m*n/hcf_function(m,n);
return lcm;
}


  
  int main(){
    unsigned long int k=0, i;
	unsigned long impossible,found;
    cin >>T;
	unsigned long lcm;
    unsigned long int num[10000], smallest;
    while (T-->0){
      k++;
	  impossible = 0, found = 0;
	  cin >> N;
	  cin >> L;
	  cin >> H;
	  if (N>0) cin >> num[0];
	  smallest = num[0];
      for (i = 1; i<N; i++){
		cin>>num[i];
		if (smallest == 1) smallest = num[i];
		if (num[i]> 1 && num[i] < smallest) smallest = num[i];
      }
	  lcm=smallest;
		for(i=1; i<N; i++){
			if(num[i]!=1) lcm=lcm_function(lcm,num[i]);
	  }


		for( i = (smallest - L%smallest) +L ;i<=H;)
		{

		impossible = 0;
			for (int j=0;j<N;j++)
			{
				if (num[j]%i !=0 && i%num[j] !=0)
				{  impossible = 1;
				   break;
				}
			}
			if (!impossible) break;
			i = i+smallest;
		}
	  
	  cout << "Case #" << k << ": ";
	  if(impossible) cout << "NO" <<endl;
      else cout << i << endl;
	}
    return 1;
  }

