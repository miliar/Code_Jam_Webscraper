#include<iostream>
#include<fstream>
using namespace std;

struct Label{
	char color;
	int pos;
};

int cmp (const void * a, const void * b) 
{  //compare的返回值应表示a>b 或a==b 或 a<b 你可用正数、0、负数表示，只要返回值包含了这三种取值就行了，一般情况下，常返回两数相减的结果
  return ( *(int*)a - *(int*)b );
}

int main()
{

	int Num,n,m;
	ofstream output("out.txt", ios::out|ios::trunc);
	ifstream cin("in.txt",ios::in);
	int * candy;
	int * sortcandy;



	cin>>Num;

	for(int num = 1; num <= Num; num ++){
		cin >> n;
		candy = new int[n];
		int allxor = 0;
		int allsum = 0;
		for(int i = 0; i < n; i ++){
			int nowCandy;

			cin >> nowCandy;
			candy[i] = nowCandy;
			allxor ^= nowCandy;
			allsum += nowCandy;

		}

		if(allxor != 0){
			cout<<"Case #"<<num<<": "<<"NO"<<endl;
			output<<"Case #"<<num<<": "<<"NO"<<endl;
			delete []candy;
			continue;
		}

		qsort(candy,n,sizeof(int),cmp);
		
		cout<<"Case #"<<num<<": "<<allsum-candy[0]<<endl;
		output<<"Case #"<<num<<": "<<allsum-candy[0]<<endl;
		delete []candy;

	}


		

	

	

	output.close();
	cin.close();

	return 0;

}



			
			





