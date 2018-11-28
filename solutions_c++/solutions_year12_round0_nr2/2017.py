#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
using namespace std;

int getBestPoints(int totalPoints, bool isSurprising){
	int bestPosibleScore=0;
	int bi, bj, bk;
	for(int i=10; i>=0; i--){
		for(int j=10; j>=0; j--){
			for(int k=10; k>=0; k--){
				if(totalPoints-i-j-k==0){
					int max=(i>j?(i>k?i:k):(j>k?j:k));
					int min=(i<j?(i<k?i:k):(j<k?j:k));
					if(abs(max-min)<2 || (abs(max-min)==2 && isSurprising)){
						
						if(max>bestPosibleScore){
							bestPosibleScore=max;
							bi=i; bj=j; bk=k;
						}
					}
				}
			}
		}
	}
	//cout<<totalPoints<<" "<<bestPosibleScore<<" "<<bi<<" "<<bj<<" "<<bk<<endl;
	return bestPosibleScore;
}


int main(int argc, char *argv[]) {
	ifstream input("/home/pabratte/Downloads/B-large.in");
	if(!input){
		cerr<<"ERROR"<<endl;
	}
	
	// los mejores puntajes posibles para cada total
	vector<int> bestPosibleScore;
	vector<int> bestPosibleScoreSurprising;
	for(int i=0; i<=30; i++){
		bestPosibleScore.push_back(getBestPoints(i, false));
		bestPosibleScoreSurprising.push_back(getBestPoints(i, true));
	}
	
//	for(int i=0; i<=30; i++){
//		cout<<i<<" "<<bestPosibleScore[i]<<" "<<bestPosibleScoreSurprising[i]<<endl;
//	}
	
	
	int nTestCases, nGooglers, nSurprisingTriplets, minBestResult, iGooglerPoints;
	input>>nTestCases;
	
	vector<int> totalPoints;
	vector<int> resultSurprisingCandidates;
	unsigned nBestResults;
	for(int i=0; i<nTestCases; i++){
		totalPoints.clear();
		resultSurprisingCandidates.clear();
		nBestResults=0;
		
		input>>nGooglers>>nSurprisingTriplets>>minBestResult;
		for(int j=0; j<nGooglers; j++){
			input>>iGooglerPoints;
			totalPoints.push_back(iGooglerPoints);
		}
		
		for(unsigned j=0; j<nGooglers; j++){
			if(bestPosibleScore[totalPoints[j]]>=minBestResult){
				// si cumple con el resultado, lo contamos
				nBestResults++;
			}else{
				// sino, si con un resultado sorpresivo puede cumplir y aun nos quedan resultados sorpresivos, lo contamos
				if(bestPosibleScoreSurprising[totalPoints[j]]>=minBestResult && nSurprisingTriplets>0){
					nBestResults++;
					nSurprisingTriplets--;
				}
			}
		}
		
		cout<<"Case #"<<i+1<<": "<<nBestResults<<endl;
	}
	input.close();
	
	return 0;
}
