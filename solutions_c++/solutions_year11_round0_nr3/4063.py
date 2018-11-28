#include<iostream>

using namespace std;


int num[1100];
int flag[1100];
int N;
int best = -1;

void cal()
{
	int left = -1;
	int right = -1;

	int leftValue = 0;
	int rightValue = 0;

	for (int i = 0; i < N; i ++)
	{
		if(flag[i] == 1) {
			//cout <<"num "<<i<<"is 1"<<endl;
			if(left == -1) { left = 0; }
			//cout<<"left = "<<left<<"  and left ^ num[i] = "<<left<<" ^ "<<num[i]<<" = ";
			left = left ^ num[i];
			//cout<<left<<endl;

			leftValue += num[i];
		} else if(flag[i] == 0) {
			//cout <<"num "<<i<<"is 0"<<endl;
			if(right == -1) { right = 0; }
			//cout<<"right = "<<right<<"  and right ^ num[i] = "<<right<<" ^ "<<num[i]<<" = ";
			right = right ^ num[i];
			//cout<<right<<endl;

			rightValue += num[i];
		}
	}

	//cout<<"left = "<<left<<"  right = "<<right<<endl;

	if(left == -1 || right == -1) { return; }

	if(left == right) {
		if( leftValue > best) {
			best = leftValue;
		} 

		if( rightValue > best) {
			best = rightValue;
		}
	}
}

void recursive(int posi)
{
	if(posi >= N) {
		cal();
		return;
	}

	flag[posi] = 0;
	recursive(posi + 1);

	flag[posi] = 1;
	recursive(posi + 1);
}

void deal()
{
	memset(num,0,sizeof(num));
	memset(flag,0,sizeof(flag));
	best = -1;

	for (int i = 0; i < N; i ++) 
	{
		cin>>num[i];
	}

	recursive(0);
	if(best == -1) {
		cout<<"NO"<<endl;
	} else {
		cout<<best<<endl;
	}
}


int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("Out.txt", "w", stdout);

	int cases	= 0;

	cin>>cases;

	for (int i = 1; i <= cases; i ++)
	{
		cin>>N;
		cout<<"Case #"<<i<<": ";
		deal();
	}
	return 0;
}
