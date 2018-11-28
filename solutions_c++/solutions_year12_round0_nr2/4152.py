#include <iostream>
#include <vector>
#include <string>
class Case{
	private:

	int max,surprisingTriplets,numberofGooglers;
	std::vector<int> scores;
	int surpriseCount;
	int answer;
	public:

	Case(int g, int s, int m){
		max = m;
		surprisingTriplets = s;
		numberofGooglers = g;
		surpriseCount = 0;
		answer = 0;
	}
	
	void addScore(int s){
		scores.push_back(s);
	}
	
	int getResult(){
		return answer;
	}
	void solve(){
		for(int i = 0 ; i < numberofGooglers ; ++i){
			int score = scores.at(i);
			int base = score - max;
			/*if(base < (2*max-4))
				continue;
			else if(base == (2*max-4) || base == (2*max-3)){
				surpriseCount++;
				answer++;
			}else{
				++answer;
			}*/
			/*if(max != 0 && score <(3*max-4))
				continue;
			else if(score == (3*max-4) || score == (3*max-3)){
				surpriseCount++;
				answer++;
			}else{
				++answer;
			}*/
			if(score<max)
				continue;
			double ratio = max - (double)base/2;
			if(max == 0 || ratio<1.5)
				answer++;
			else if(ratio<=2){
				answer++;
				surpriseCount++;
			}else
				continue;
			
		}
		if(surpriseCount > surprisingTriplets){
			answer = answer - (surpriseCount-surprisingTriplets);
		}
	}
};

int main(){
	int m,s,g;
	char *in = "B-large.in";
	char *out ="result.out";
	int testCases;
	std::vector<Case *> cases;
	freopen(in,"rt",stdin);
	freopen(out,"wt",stdout);
	scanf("%d",&testCases);
	for(int i=0 ; i<testCases;++i){
		int score;
		scanf("%d %d %d",&g,&s,&m);
		Case *temp = new Case(g,s,m);
		for(int j = 0; j<g ; ++j){
			scanf("%d",&score);
			temp->addScore(score);
		}
		cases.push_back(temp);
	}
	for(int i = 0 ; i < cases.size() ; ++i){
		cases.at(i)->solve();
		std::cout<<"Case #"<<i+1<<": "<<cases.at(i)->getResult()<<std::endl;
	}
	return 0;
}

