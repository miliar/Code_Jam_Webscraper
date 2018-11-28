#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

char data[8100];
char featuretmp[8100];
int len = 0;
vector<pair<string,int> > features;

int prop[8100];

struct node {
	double w;
	int featnum;
	node *left;
	node *right;
} pre[100000], *root;
int precnt;

int pos;
node *buildtree(){
	int i;
	node *curnod = &pre[precnt];
	curnod->featnum = -1;
	curnod->left = NULL;
	curnod->right = NULL;
	curnod->w = 1;
	precnt ++;
	int flg = 0;
	for(;pos < len;pos++){
		if(data[pos] == '('){
			sscanf(data+pos+1,"%lf",&(curnod->w));
		}
		if(data[pos] == ' '){
			if(flg == 2){
				curnod->left = buildtree();
				curnod->right = buildtree();
			}
			flg = 1;
		}
		if(data[pos] >= 'a' && data[pos] <= 'z' && flg == 1){
			flg = 2;
			sscanf(data+pos,"%s",featuretmp);
			for(i=0;i<features.size();i++){
				if(features[i].first.compare(featuretmp) == 0){
					curnod->featnum = i;
					break;
				}
			}
			if(i >= features.size()){
				curnod->featnum = i;
				features.push_back(make_pair(featuretmp,i));
			}
		}
		if(data[pos] == ')'){
			pos++;
			break;
		}
	}
	return curnod;
}

double trace(node *cur){
	if(cur->featnum != -1){
		if(prop[cur->featnum]){
			return cur->w * trace(cur->left);
		}else{
			return cur->w * trace(cur->right);
		}
	}
	return cur->w;
}

int main(){
	int TTT,testnum;
	scanf("%d",&TTT);
	for(testnum=1;testnum<=TTT;testnum++){
		int L;
		features.clear();
		memset(data,0,sizeof(data));
		scanf("%d%*c",&L);
		len = 0;
		precnt = 0;
		while(L--){
			gets(data+len);
			for(;data[len];len++);
		}
		pos = 0;
		root = buildtree();
		sort(features.begin(),features.end());

		printf("Case #%d:\n",testnum);
		int a;
		int i;
		scanf("%d",&a);
		for(i=0;i<a;i++){
			int n;
			memset(prop,0,sizeof(prop));
			scanf("%*s%d",&n);
			while(n -- > 0){
				pair<string,int> tmptmp;
				scanf("%s",featuretmp);
				tmptmp.first = featuretmp;
				tmptmp.second = -1;
				vector<pair<string,int> >::iterator tmp = lower_bound(features.begin(),features.end(),tmptmp);
				if(tmp != features.end()){
					prop[tmp->second] = 1;
				}
			}
			printf("%.10lf\n",trace(root));
		}
	}
	return 0;
}
