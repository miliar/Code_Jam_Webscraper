# include<iostream>
# include<fstream>
# include<strstream>
using namespace std;

int main(){
	ifstream fin("C-large.in");
	char buffer[100];
	fin.getline(buffer,100);
	int n=atoi(buffer);
	if(n>=1&&n<=50){
		ofstream myfile;
		myfile.open("output.txt");
		for(int g=0;g<n;g++){
			long int a,b;
			char b1[20],b2[20];
			for(int f=0;f<20;f++){
				b1[f]=0;
				b2[f]=0;
			}
			for(int f=0;f<100;f++){
				buffer[f]=0;
			}
			fin.getline(buffer,100);
			int q=strlen(buffer);
			int o=0;
			while(buffer[o]!=' '){
				b1[o]=buffer[o];
				o++;
			}
			a=atoi(b1);
			int p=0;
			while(o!=q){
				b2[p++]=buffer[o];
				o++;
			}
			b=atoi(b2);
			int ans=0;
			if((a>=1&&a<=b)&&(b<=2000000)){
				for(long int i=a;i<=b;i++){
					long int num1=i;
					long int num2=0;
					long int num3=0;
					int count=0;
					while(num1!=0){
						count++;
						num1/=10;
					}
					num1=i;
					num2=num1;
					do
					{
						int k=10;
						int count1=0;
						int s=k;
						while(s!=0){
							count1++;
							s/=10;
						}
						long int z=num2%k;
						long int y=num2/k;
						s=10;
						for(int d=0;d<(count-count1);d++){
							s*=10;
						}
						num3=(z*s)+y;
						num2=num3;
						if((num1<num3)&&(num3<=b)){
							ans++;
							num2=num3;
						}
					}while(num2!=num1);
				}
			}
			myfile<<"Case #"<<g+1<<": "<<ans<<"\n";
		}
		myfile.close();
	}
	return 0;
}
