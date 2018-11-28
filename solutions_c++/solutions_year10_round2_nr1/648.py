#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <math.h>

using namespace std;

const long long MAX = 1000000;
int nTestCases;
fstream	fin;
fstream fout;

int N, M;
char oldPath[101][101];
char newPath[101][101];

struct NODE{
	char name[101];
	int length;
	int child[301];
	int size;
};

NODE node[MAX];
int nodeSize;

int pos[301];

int addNode(char *pth){
	int oldNodeSize = nodeSize;
	int cnt=0;
	int i;
	for(i=0; pth[i]; i++){
		if(pth[i]=='/')
			pos[cnt++] = i;
	}
	pos[cnt] = i;
	
	int nodeId=0;
	int level = 0;
	while(1){
		int i;

		int oldSize = node[nodeId].size;
		for(i=0; i<node[nodeId].size; i++){
			bool found = false;
			int cNode = node[nodeId].child[i];
			if(node[cNode].length == (pos[level+1]-pos[level]-1)){
				int k;
				for(k=0; k<node[cNode].length; k++)
					if(pth[pos[level]+1+k] != node[cNode].name[k])
						break;
				if(k==node[cNode].length)
					found = true;
			}
			if(found){
				nodeId = cNode;
				level++;
				break;
			}
		}
		
		if(i==oldSize){
			while(level<cnt){
				node[nodeId].child[node[nodeId].size] = nodeSize;
				node[nodeId].size++;
				int k;
				for(k=0; k< pos[level+1]-pos[level]-1; k++)
					node[nodeSize].name[k] = pth[pos[level]+1+k];
				node[nodeSize].name[k] = 0;
				node[nodeSize].length = pos[level+1]-pos[level]-1;
				node[nodeSize].size = 0;
				node[nodeSize].child[0] = nodeSize+1;
				nodeId=nodeSize;
				nodeSize++;
				level++;
			}
			break;
		}
	}

	return (nodeSize - oldNodeSize);
}

void init(){
	fin >> N >> M;
	for(int i=0; i<N; i++)
		fin >> oldPath[i];
	for(int i=0; i<M; i++)
		fin >> newPath[i];

	nodeSize=1;
	strcpy(node[0].name, "/");
	node[0].length = 1;
	node[0].size = 0;
	for(int i=0; i<N; i++)
		addNode(oldPath[i]);
}



void main()
{
	fin.open("z:\\input.txt", ifstream::in);
	fout.open("z:\\output.txt", ifstream::out);


	fin >> nTestCases;

	for(int testCase = 1; testCase <= nTestCases; testCase++){
		init();

		int cnt = 0;
		for(int i=0; i<M; i++)
			cnt += addNode(newPath[i]);
		
		fout << "Case #" << testCase <<": " << cnt << endl;
	}

	fin.close();
	fout.close();
}