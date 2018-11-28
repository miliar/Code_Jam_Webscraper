#include <stdio.h>
#include <map>

#define dprintf(...)

using namespace std;

typedef map<char,void*> node;

node begin;

void addword(char* tmp) {
	node* cur=&begin;
	node* new_node;
	node::iterator it;
	while(*tmp) {
		it=cur->find(*tmp);
		if(it==cur->end()) {
			cur->insert(make_pair(*tmp,new_node=new node));
			cur=new_node;
		} else {
			cur=(node*)(it->second);
		}
		tmp++;
	}
	cur->insert(make_pair(*tmp,(void*)NULL));
}

int process_line(node* cur, char *line,int len, int lim) {
	node::iterator it;
	char* end;
	int occur=0;
	if((cur)==NULL) {
		if(len==lim)
			return 1;
		return 0;
	}
	len++;
	dprintf("letter %c\n",*line);
	fflush(NULL);
	if((*line)=='(') {
		end=++line;
		while((*end++)!=')');
		while(((*line)!=')')&&((*line)!=0)) {
			it=cur->find(*line);
			dprintf("( letter %c\n",*line);
			if(it!=cur->end()) {
				occur+=process_line((node*)(it->second),end,len,lim);
			}
			++line;
		}
	} else {
		it=cur->find(*line);
		if(it!=cur->end()) {
			occur+=process_line((node*)(it->second),line+1,len,lim);
		}
	}
	return occur;
}

int main(void) {
	int length=0;
	int words=0;
	int cases=0;
	int i=0,j=0;
	char tmp;
	char buffer[1024];
	if(!scanf("%d %d %d",&length,&words,&cases)) return 1;
	dprintf("%d %d %d\n",length,words,cases);
	for(i=0;i<words;i++) {
		if(!scanf("%s",buffer)) return 2;
		dprintf("adding %d/%d (%s)\n",i,words,buffer);
		addword(buffer);
	}
	for(i=0;i<cases;i++) {
		if(!scanf("%s",buffer)) return 3;
		dprintf("processing %d/%d (%s)\n",i,cases,buffer);
		printf("Case #%d: %d\n",i+1,process_line(&begin,buffer,0,length+1));
	}
	return 0;
}


