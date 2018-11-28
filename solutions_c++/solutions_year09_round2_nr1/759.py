#include <stdio.h>
#include <map>
#include <set>
#include <string>
#include <ctype.h>

#define dprintf(...) printf(__VA_ARGS__)
#define dprintf(...)

using namespace std;

typedef set<string> animal;

struct node {
	float p;
	string feature;
	node* first;
	node* second;
};

node* create_tree(const char** tree) {
	node* result;
	static char buff[1024];
	float p;

	dprintf("Processing tree '%s'...\n",*tree);
	while((**tree)==' ') ++(*tree);
	(*tree)++;
	result=new node;
	while((**tree)==' ') ++(*tree);
	sscanf(*tree,"%f",&(result->p));
	while(isdigit(**tree) || ((**tree)=='.')) ++(*tree);
	dprintf("Got prob %f, processing '%s'...\n",result->p,*tree);
	while((**tree)==' ') ++(*tree);
	result->feature="";
	while(isalpha(**tree)) {
		result->feature+=*((*tree)++);
	}
	dprintf("Got name '%s', processing '%s'...\n",result->feature.c_str(),*tree);
	while((**tree)==' ') ++(*tree);
	if((*((*tree)))==')') {
		result->first=NULL;
		result->second=NULL;
		dprintf("Ending value %f\n",result->p);
	} else {
		result->first=create_tree(tree);
		result->second=create_tree(tree);
		dprintf("Feature '%s' with value %f\n",result->feature.c_str(),result->p);
		while((**tree)==' ') ++(*tree);
	}
	(*tree)++;
	return result;
}

animal read_animal() {
	animal an;
	static char buff[1024];
	int feat,i;
	scanf("%s %d",buff,&feat);
	dprintf("Animal '%s' has %d features\n",buff,feat);
	for(i=0;i<feat;i++) {
		dprintf("And the %d. feature is....\n",i);
		scanf("%s",buff);
		dprintf("\t%s\n",buff);
		an.insert(buff);
	}
	while(getchar()!='\n');
	return an;
}

void print_cuteness(node* tree, const animal an) {
	float p=1;
	while(tree) {
		p=p*(tree->p);
		if(an.find(tree->feature)!=an.end()) {
			dprintf("This animal has feature '%s'\n",tree->feature.c_str());
			tree=tree->first;
		} else {
			dprintf("This animal doesn't have feature '%s'\n",tree->feature.c_str());
			tree=tree->second;
		}
	}
	printf("%1.7f\n",p);
}

void getline(string& buff) {
	char tmp;
	while((tmp=getchar())!='\n')
		buff+=tmp;
}

int main(void) {
	int cases=0;
	int lines=0;
	int i,j;
	const char *tmp;
	string tmp_line;
	node* tree=NULL;
	animal an;
	scanf("%d\n",&cases);
	dprintf(" * %d cases\n", cases);
	for(i=1;i<=cases;i++) {
		tmp_line="";
		scanf("%d\n",&lines);
		dprintf("%d. case has tree %d lines long\n",i,lines);
		for(j=0;j<lines;j++) {
			getline(tmp_line);
		}
		dprintf("Tree is '%s'\n",tmp_line.c_str());
		tree=create_tree(&(tmp=tmp_line.c_str()));
		scanf("%d\n",&lines);
		dprintf("%d. case has %d animals\n",i,lines);
		printf("Case #%d:\n",i);
		for(j=0;j<lines;j++) {
			an=read_animal();
			print_cuteness(tree, an);
		}
	}
	return 0;
}
