#include < iostream >
#include < fstream.h >
#include < iomanip.h >
#include < cstdlib >
#include < string.h >

void main( void )
{
	int i,j,k,tag,flag,max,Case,Switch,S,Q;
	ifstream inData;
	ofstream outData;
	inData.open("A-small-attempt0.in");
	outData.open("A-small-attempt0.out");
	inData >> Case ; 

	for( k = 0 ; k < Case ; k++ ){
		inData >> S;
		char **SearchE = new char*[S];
		for( i = 0 ; i < S ; i++ ){
			SearchE[i] = new char[100];
		}
		inData.ignore(100,'\n');
		for( i = 0 ; i < S ; i++ ){
			inData.getline( SearchE[i] , 100);
		}
		inData >> Q ;
		char **Queries = new char*[Q];
		for( i = 0 ; i < Q ; i++ ){
			Queries[i] = new char[100];
		}
		inData.ignore(100,'\n');
		for(i = 0 ; i < Q ; i++ ){
			inData.getline( Queries[i] , 100);
		}
		

		int *S_tag = new int[S];
		tag = 0 ; Switch = 0 ; flag = 1;

		while( flag!=0 ){
			memset( S_tag , 0 , sizeof(int)*S );
			for( i = 0 ; i < S ; i++ ){
				for( j = tag ; j < Q ; j++ ){
					if( strcmp( SearchE[i] , Queries[j] ) == 0 && S_tag[i] == 0 ){
						S_tag[i] = j + 1 ;       
					}
				}
			}
			Switch++;
			for( i = 0 ; i < S ; i++ ){
				if( S_tag[i] == 0 ){
					flag = 0; Switch--;
					break;
				}
			}			

			max = S_tag[0]; tag = max - 1;
			for( i = 1 ; i < S ; i++ ){
				if( S_tag[i] > max ){
					max = S_tag[i];
					tag = S_tag[i] - 1;
				}	
			}
		}
		cout <<"Case #"<<k+1<<":  "<<  Switch<<endl;
		outData<<"Case #"<<k+1<<":  "<<  Switch<<endl;
		for( i = 0 ; i < S ; i++ )   
			delete[] (SearchE[i]);   
		delete[]  SearchE;
		for( i = 0 ; i < Q ; i++ )   
			delete[] (Queries[i]);   
		delete[] Queries;
		delete[] S_tag;
	}		
	inData.close();
	outData.close();
}