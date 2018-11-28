#include <iostream>
using namespace std;
int p1();
int p2();
int p3();
int p5();
int p8();
int p11();
int p10();
int p6();
int p7();
int p4();
int p9();
int p12();
int p15();
int p13();
int p19();
int p23();
int p31();
int p27();
struct haha{
	int hk;
	char a;
};

int calculate(int num, int low, int high){
	int count = 0;
	int temp=num;
	int cc = num;
	int save[10];

	int i = 0;
	int j = 0;
	while(num){
		count++;
		num /= 10;
		i++;
	}
	
	int valid = 0;
	int current; 
	save[0] = temp;
	//valid++;
	for(i=1;i<count;i++){
		int last_digit = temp % 10;
		current = last_digit *  pow(10.0,(count-1)) + temp / 10;
		temp = current;
		for(j = 0;j <i;j++){
			if(current == save[j])
				break;
		}
		save[i] = current;
		if(j!=i)
			continue;
		if(current<=high && current >=low && last_digit !=0 && current > cc){
			valid++;
		}
	}
//	cout<<cc<<" "<<valid<<endl;
	return valid;
}
int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	cin>>n;

	int i,j;
	int a,b;
	int num;
	for(int i = 1 ; i <= n; i++){
		cin>>a>>b;
		num = 0;
//		cin>>j;
		for(j=a;j<=b;j++){
			num += calculate(j, a, b);
//			cout<<num<<endl;
		}
		
		cout<<"Case #"<<i<<": "<<num<<endl;
	}

//	p23();
	return 0;

	
}