#include<iomanip>
#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
#include<map>
#include<string.h>
#include<vector>
using namespace std;
int max(int a,int b){if (a>b) return a; return b;}
int max(int a,int b,int c){if (a>b&&a>c) return a;else if(b>c) return b;return c;}
int max(int *a,int n){int i,max=a[0]; for(i=1;i<n;i++)if(max<a[i]) max=a[i]; return max;}
int min(int a,int b){if (a<b) return a; return b;}
int min(int a,int b,int c){if (a<b&&a<c) return a;else if(b<c) return b;return c;}
int min(int *a,int n){int i,min=a[0]; for(i=1;i<n;i++)if(min>a[i]) min=a[i]; return min;}

int power(int a, int b)
{
int i,temp=1;
for(i=1;i<=b;i++)
temp=temp*a;
return temp;
}

void reversestr( char str[],int len){
    char *tempstr;int i,j,count=0;
    tempstr=(char *)malloc(sizeof(char)*(len+1));
    for(i=len-1,j=0;i>=0;i--,count++,j++)    tempstr[j]=str[i];
    tempstr[count]='\0';
    for(i=0;i<=count;i++)    str[i]=tempstr[i];
    free(tempstr);
}

int convert_to_decimal(int b,char *result){
     int ans=0,c=0;
     int i,l=strlen(result);
     for(i=l-1;i>=0;i--)
               ans+=((int)((int)result[i]-48))*(int)power((int)b,c++);                 
    return ans;

}


int sum_modulus_base(int b, char *n1, char *n2){
      int d,temp,f,s,i,l1=strlen(n1),l2=strlen(n2),maxlen=l1>l2?l1:l2;
      char *result=new char[20];
      if(l1>l2)
      {
            d=l1-l2;
            for(i=l2;i>=0;i--)
                n2[i+d]=n2[i];
            for(i=0;i<d;i++)
                 n2[i]=48;
      }
      else if(l2>l1){
           d=l2-l1;
            for(i=l1;i>=0;i--)
                n1[i+d]=n1[i];
            for(i=0;i<d;i++)
                 n1[i]=48;
      }                  
      for(i=maxlen-1;i>=0;i--){
                  f=(int)n1[i]-48;
                  s=(int)n2[i]-48;             
                  temp=f+s;
                  temp%=b;
                  result[i]=temp+48;
                  
                  l1--; l2--;          
      }
      result[maxlen]='\0';
     return convert_to_decimal(b,result);
}

char* convert_to_base(int b, int num){
      char *num1=new char[20];
       int i=0;
       while(num>0)
       {
            num1[i++]=(char)(num%b+48);
            num/=b;
       }
       num1[i]='\0';                  
      reversestr(num1,i);
      return num1;
      
}

inline int no_of_digits(int number)
{
int count=0;
    while(number>0){
    number=number/10;
    count++;
}
return count;
}



int convert_string_to_number(char a[]){
	int s,length,sum=0,count=0,flag=1;
		
	length=strlen(a);
	
	while(length--){
		switch((int)a[length]){
			case 48:
				count++; 
				break;
			case 49:	
				sum+=power(10,count);
				count++; break;
			case 50:
				sum+=2*power(10,count);
				count++; break;
			case 51:
				sum+=3*power(10,count);
				count++; break;
			case 52:
				sum+=4*power(10,count);
				count++; break;
			case 53:
				sum+=5*power(10,count);
				count++; break;
			case 54:
				sum+=6*power(10,count);
				count++; break;
			case 55:
				sum+=7*power(10,count);
				count++; break;
			case 56:
				sum+=8*power(10,count);
				count++; break;
			case 57:
				sum+=9*power(10,count);
				count++; break;
			default:
				flag=0;
				break;
						
		}
		if(flag==0)
			break;
			
	}
	if(flag==0)
		return -99;

	else 
	return sum;
}




int main(){
   freopen("F:/codejaminput.txt","r",stdin);
    freopen("F:/codejamoutput.txt","w",stdout);
    int i,j,k,n; 
    long double RPI[105],opponents[105],WP[105],OWP[105],OOWP[105];
    char arr[105][105];
    int t;
    cin>>t;
    for(k=1;k<=t;k++){
           cin>>n;           
           
           for(i=0;i<n;i++){
                cin>>arr[i];
                //cout<<arr[i]<<;     
           }
           
           
           for(i=0;i<n;i++)
           {
               opponents[i]=0;            
               long double  wins=0.0;            
               for(j=0;j<n;j++)
               if(i!=j){
                   if(arr[i][j]=='1'){
                        wins++;
                        opponents[i]++;
                   }
                   else if(arr[i][j]=='0')
                   {
                        opponents[i]++;
                   }
                   
                            
               }   
               if(opponents[i]==0)
                    WP[i]=0;
               else 
               WP[i]=wins/opponents[i];             
                           
           }
              
           for(i=0;i<n;i++)
           {
               //cout<<endl;            
               long double c=0.0;  

               long double total=0.0,ow=0.0;           
               for(j=0;j<n;j++){
                                
                     ow=0.0; c=0.0;           
                    if(i!=j&&(arr[i][j]=='0'||arr[i][j]=='1')){
                         for(int l=0;l<n;l++)
                         {
                             if(j!=l&&l!=i&&(arr[j][l]=='0'||arr[j][l]=='1'))
                        
                        
                                 if(arr[j][l]=='1'){
                                       ow++;
                                       c++;
                                  }
                                  else if(arr[j][l]=='0'){
                                        c++;
                                  }
                           
                           
                     //      cout<<ow<<endl;
                         }
                     
                     
                     
                     long double tempans=0.0;
                     if(c!=0.0)
                     tempans=ow/c;
                   //  cout<<"OW of "<<j<<" leaving out"<< i <<" "<<tempans<<endl;
                     total+=tempans;
                     }
               }
               OWP[i]=total/opponents[i];
            //  cout<<endl;
           }        
               
           for(i=0;i<n;i++)
           {
                 
           long double oow=0.0;              
               for(j=0;j<n;j++)
               if(i!=j){
                    if(arr[i][j]=='1'||arr[i][j]=='0'){
                           oow+=OWP[j];
                     
                         
                    }
               
               }
               
               OOWP[i]=oow/opponents[i];
          //  cout<<OOWP[i]<<endl<<endl;
                           
           }
          printf("Case #%d:\n",k);
          for(i=0;i<n;i++)
          {
           //cout<<setprecision(12)<<WP[i]<<" "<<opponents[i]<<" "<<OWP[i]<<" "<<OOWP[i]<<endl;               
           long double answer=0;
           long double x=0.25,y=0.5;
           answer+=x*WP[i];
           answer+=y*OWP[i];
           answer+=x*OOWP[i];
           
           //cout<<"ans="
           cout<<setprecision(12)<<answer<<endl;
           //prinf\n",answer);
           }
           
               
    }
      




    
    return 0;
}
