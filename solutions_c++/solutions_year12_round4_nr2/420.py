#include<iostream>
#include<vector>
#include<string>

long N,W,L;
long mR[1010];

int mIdx[1010];
int mX[1010];
int mY[1010];


void problem(){
	std::cin >> N >> W >> L;
	bool ok[1010];
	for( int i=0;i<N;i++){
		std::cin >> mR[i];
		mX[i] = 0;
		mY[i] = 0;
		ok[i] = false;
	}
	

	for ( int i=0;i<N;++i ) {
		int idx = -1 ;
		for ( int j=0;j<N;++j ) {
			if ( !ok[j] ) {
				if ( idx == -1 ) idx = j ;
				else if ( mR[j] > mR[idx] ) idx = j ;
			}
		}
		
		mIdx[i] = idx;
		ok[idx] = true;
	}

	int x0 = 0; int y0=0; int dy = -1;

	for ( int i=0;i<N;++i ) {
		int r = mR[mIdx[i]] ;
		if ( x0 == 0 ) {
			mX[mIdx[i]] = x0, mY[mIdx[i]] = y0 ;
			dy = r ;
			x0 += r ;
		} else if ( x0 + r <= W ) {
			mX[mIdx[i]] = x0 + r ;
			mY[mIdx[i]] = y0 ;
			x0 += r*2 ;
		} else {
			y0 += dy + r ;
			mX[mIdx[i]] = 0;
			mY[mIdx[i]] = y0 ;
			x0 = r ;
		}
	}

	for( int i=0;i<N;i++ ){
		printf(" %d.0 %d.0",mX[i],mY[i]);
		//std::cout << " " << mX[i] << " " << mY[i];
	}
	

	return ;
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
		std::cout << "Case #" <<  i + 1 << ":";
		problem();
		std::cout << std::endl;
	}

	return 0;
}