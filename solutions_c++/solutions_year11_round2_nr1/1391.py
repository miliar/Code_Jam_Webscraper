//google code jam 2011 round 1b problem a
#include <stdio.h>

class Team{
public:	
	const static int maxN=101;
	double wp,owp,oowp;
private:
	int winCount,loseCount, total;
	int status[maxN];
	int myIndex;

public:
	Team(int myIndex, int n, int status[]){
		this->myIndex=myIndex;
		this->winCount = this->loseCount = 0;
		for (int i=0; i<n; i++){
			this->status[i]=status[i];
			if (status[i]==1) 
				this->winCount++;
			else if(status[i]==0)
				this->loseCount++;
		}
		this->total = this->winCount + this->loseCount;
		this->wp=(double)this->winCount/this->total;
	}

	double calcWp4Owp(int index){
		int t=this->winCount;
		if (this->status[index]==1) t--;
		return (double)t/(this->total-1);
	}

	void calcOwp(int n, Team* teams[]){
		double sum=0;
		for (int i=0; i<n; i++)
			if (this->status[i]!=2)
				sum+=teams[i]->calcWp4Owp(this->myIndex);

		this->owp=sum/this->total;
	}

	void calcOOwp(int n, Team* teams[]){
		double sum=0;
		for (int i=0; i<n; i++)
			if (this->status[i]!=2)
				sum+=teams[i]->owp;
		this->oowp=sum/this->total;
	}

	double getRpi(){
		return this->wp*0.25 + this->owp*0.5 + this->oowp*0.25;
	}
};

Team* teams[Team::maxN];
int n;
void inputData(){
	char str[Team::maxN];
	int status[Team::maxN];
	scanf("%d", &n);

	for (int i=0; i<n; i++){
		scanf("%s", str);
		for (int j=0; j<n; j++){
			int t=-1;
			switch(str[j]){
				case '.':
					t=2;
					break;
				case '0':
					t=0;
					break;
				case '1':
					t=1;
					break;
			}
			status[j]=t;
		}
		teams[i]=new Team(i, n, status);
	}
}

int main(){
	int caseIndex, caseT;
	scanf("%d", &caseT);
	for (caseIndex=1; caseIndex<=caseT; caseIndex++){
		inputData();

		for (int i=0; i<n; i++)
			teams[i]->calcOwp(n, teams);
		for (int i=0; i<n; i++)
			teams[i]->calcOOwp(n, teams);

		printf("Case #%d:\r\n", caseIndex);
		for (int i=0; i<n; i++){
			double rpi=teams[i]->getRpi();
			printf("%.10lf\r\n", rpi);
		}
	}

	return 0;
}