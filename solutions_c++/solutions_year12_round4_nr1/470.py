#include<iostream>
#include<vector>
#include<string>
#include<queue>



long num;
long mPosition[10010];
long mLength[10010];
long mReach[10010];
long mLengthOfDistance;


std::string problem(){

	std::cin >> num;

	for(long i=0;i<num;i++){
		long pos,len;
		std::cin >> mPosition[i] >> mLength[i];
		mReach[i] = 0;
	}

	std::cin >> mLengthOfDistance;

	mReach[0] = mPosition[0];
	for( int i=0;i<num;i++){
		int reachable = mPosition[i] + mReach[i];
		if( reachable >= mLengthOfDistance )
			return "YES";
	
		for( int j=i+1; j<num ; j++ ){
			if(  mPosition[j] > reachable ) break;
			int distance = mPosition[j] - mPosition[i];
			int newReach = 0;
			if( mLength[j] >= distance )
				newReach = distance;
			else
				newReach = mLength[j];
			if( newReach > mReach[j] ) 
				mReach[j] = newReach;
		}
	}

	return "NO";
}

int main(int argc,char** argv){
	int numOfProblem;

	if( argc > 2 ){
		freopen(argv[1],"r",stdin);
		freopen(argv[2],"w",stdout);
	}else{
		std::string filename;
		std::cin >> filename;
		freopen(filename.c_str() ,"r" ,stdin );
		freopen(filename.append(".out.txt").c_str(),"w",stdout);
	}

	std::cin >> numOfProblem;

	for( int i=0;i<numOfProblem;i++){
		std::cout << "Case #" <<  i + 1 << ": "  << problem() << std::endl;
	}

	return 0;
}
