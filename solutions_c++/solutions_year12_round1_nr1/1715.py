#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>

using namespace std;


int main()
{
	int numCases, A, B;
	cin>>numCases;
	for(int i = 0; i < numCases; i++)
	{
		cin>>A;
		cin>>B;
		vector<float> probabilityRight;
		float temp;
		for(int k = 0; k < A; k++)
		{
			cin>>temp;
			probabilityRight.push_back(temp);
		}
		/*
		printf("A: %d B: %d\n", A, B);
		
		for(int k = 0; k<probabilityRight.size(); k++) {
			printf("%f ", probabilityRight[k]);
		}
		printf("\n");
		*/		
		
		float minStrokes = 999999;
		//First row, keystrokes if keep typing.
		float keepTyping = 0;
		float probRightAll = 1;
		for(int k = 0; k < A; k++)
		{
			probRightAll = probRightAll * probabilityRight[k];
		}
		int keyStrokesAfterIfRight = (B - A) + 1; 		//1 enter
		int keyStrokesAfterIfWrong = (B - A) + B + 2;   //2 for the two enters required.

		keepTyping = (probRightAll * keyStrokesAfterIfRight) + (1 - probRightAll) * keyStrokesAfterIfWrong;
		minStrokes = keepTyping;
//		printf("keep Typing expected: %f\n\n", keepTyping);
		

		vector<float> cumProb;
		//new new new
		//preprocess cumulative probabilities
		cumProb.push_back(1 - probabilityRight[0]);
//			printf("[%f]", cumProb.back());
		for(int k = 1; k < A; k++)	
		{
			cumProb.push_back((1-cumProb[k-1]) * (1-probabilityRight[k]));
//			printf("[%f]", cumProb.back());
		}
//		printf("\n");

	
		vector<float> probs;
		for(int k = 1; k <= A; k++)
		{
			float sum = 0;
			int count = (B-A) + 2*k +1;
		//	printf("\t%d:(%f) %d\n", -1,probRightAll, count);
			sum+= count * (probRightAll);
			for(int z = 0; z < A; z++) //how far back the error is.
			{
				int count = 0;
				//error deleted
				if(k>(A-z-1))
				{
					count = (B-A) + 2 * (k) + 1;
//					printf("!");
				}
				else
				{
					count = (B-A) + 2 * (k) + 1 + B + 1;
//					printf("?");
				}
//				printf("\tError at index A-%d: keystrokes %d\n", z, count);
				sum+=cumProb[z]*count;
			}
			if(sum < minStrokes)
				minStrokes = sum;
			
//			printf("Backspaces #%d ]  expected value: %f\n",k, sum);
		}
		int enter = (B + 2);
		if(enter < minStrokes)
			minStrokes = enter;
//		printf("%f\n", minStrokes);
		
//	printf("-------\n\n");
		printf("Case #%d: %f\n", i+1, minStrokes);	
	}
}
