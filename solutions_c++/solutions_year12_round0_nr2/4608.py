#include<fstream>
using namespace std;

int main(){
	//variables
	int t, N, S, p, count, i, j, total, max_score;
	ifstream fin ("B-large.in");
	ofstream fout ("B-large.out");
		
	//reading data
	fin>>t;
	
	//for each test case
	for(i = 1; i <= t; i++){
		count = 0;
		
		//read  more data
		fin>>N>>S>>p;
		
		//count how many googlers "qualify"
		for(j = 1; j <= N; j++){
			fin>>total;
			//NOT SURPRISE
			if(total%3 == 0)
				max_score = total/3;
			else
				max_score = total/3 +1;
			
			if(max_score >= p)
				count++;
			else //considering SURPRISE
				if(S){
					if(total >= 3 && total%3 < 2)
						max_score = total/3 + 1;
					else
						if(total%3 == 2)
							max_score = total/3 + 2;
					if(max_score == p){
						count++;
						S--;
					}
				}
				
		}  	
		//write result
		if(i > 1)
			fout<<'\n';
		fout<<"Case #"<<i<<": "<<count;
		
	}
	
	//close everything
	fin.close();
	fout.close();
	
	//done!
	return 0;
}