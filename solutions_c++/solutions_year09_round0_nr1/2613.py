#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <vector>

using namespace std;

char** match(char* buf, int depth, const vector< map< string, int> >& tokenss ,int& flag) 
{
    char *p1 = NULL;
    int j = 0;
    char* r = NULL;
    if(buf[0] == 0) {
	return 0;
    }
    int max = 0;
    if(buf[0] == '(') {
	p1 = strchr(buf,')');
	if(p1 == NULL) {
	    printf("missing ) ");
	    return 0;;
	}
	*p1 = 0;
	buf = buf+1;
	r = new char[p1-buf+1];
	memcpy(r,buf,p1-buf);
	r[p1-buf] = 0;
	j = p1-buf;
	max = p1-buf;
    } else {
	max = 1;
	r = new char[2];
	r[0] = buf[0];
	r[1] = 0;
	p1 = buf;
	j = 1;
    }

    depth--;
    char** ret_tmp = NULL;
    ret_tmp = match(p1+1, depth, tokenss,flag);
    if(flag == 0) {
	return 0;
    }
    int length = 0;
    int i = 0;
    char** ret;
    if(ret_tmp != 0) {
	for(i = 0;  ; i++) {
	    if(ret_tmp[i] == 0) {
		break;
	    }
	}
	length = i;
	ret = new char*[length*j+1];
	memset(ret, '\0',(length*j+1)*sizeof(char*));

    } else {
	length = 0;
	ret = new char*[j+1];
	memset(ret, '\0',(j+1)*sizeof(char*));

    }
    int x = 0;
    for(int m = 0; ; m++) {
	if(r[m] == 0) {
	    break;
	}
	if(length == 0) {
	    char buf[16];
	    memset(buf,'\0', (16));
	    memcpy(buf,&(r[m]),1);
	    ret[x] = new char[1+1];
	    memcpy(ret[x], buf, 1);
	    ret[x][1] = 0;
	    x++;

	} else {
	    for(int n = 0; ;n++) {
		if(ret_tmp[n] == 0) {
		    break;
		}
		char buf[15+1];
		memset(buf,'\0',16);
		memcpy(buf,&(r[m]),1);
		memcpy(&(buf[1]),ret_tmp[n],strlen(ret_tmp[n]));
		map<string,int>::const_iterator it = tokenss[depth].find(string(buf));
		if(it == tokenss[depth].end()) {
		    continue;
		}
		ret[x] = new char[strlen(ret_tmp[n])+1+1];
		memcpy(ret[x], buf, strlen(ret_tmp[n])+1);
		ret[x][strlen(ret_tmp[n])+1] = 0;
		x++;
	    }
	}
    }
    if(x == 0) {
	delete ret;
	ret = 0;
	flag = 0;
    }
    for(int i = 0; i<length ; i++) {
	if(ret_tmp[i] != 0) {
	    delete ret_tmp[i];
	} else {
	    break;
	}
    }
    delete ret_tmp;
    delete r;
    return ret;
}

int main()
{
    FILE *fp;
    fp = fopen("./a.txt","r");
    if(fp == NULL){
	return 0;
    }
    char buf[1024];
    memset(buf,'\0',1024);
    int caseid = 1;
    while(fgets(buf,1024,fp)) {
	char *p1 = NULL;
	char *p2 = NULL;
	p1 = buf;
	int i = 0;
	int m = 0;
	int n = 0;
	int r = 0; 
	for(i = 0; i < 2; i++) {
	    p2 = strchr(p1,' ');
	    if(p2 == NULL) {
		break;
	    }
	    if(i == 0) {
		m = atoi(p1);
	    } else if (i == 1) {
		n = atoi(p1);
	    }
	    p1 = p2+1;
	}
	if(i != 2) {
	    return 0;
	}
	r = atoi(p1);
	char buf2[1024];
	i = 0;
	int depth = m;
	vector<map<string, int> > tokenss(depth);	
	int count = 0;
	while(fgets(buf2,1024,fp) && i < (n+r) ) {
	    if(i < n) {
		int j = 0;
		for(j = strlen(buf2); j >= 0; j--) {
		    if(buf2[j-1] == '\r' || buf2[j-1] == '\n' ) {
		    } else{ 
			break;
		    }
		}
		buf2[j] = 0;
		for(int m1 = 0; m1 < depth; m1++) {
		    tokenss[m1].insert(map<string,int>::value_type(string(buf2+j-1-m1),0));
		}
	    } else {
		int j = 0;
		count = 0;
		for(j = strlen(buf2); j >= 0; j--) {
		    if(buf2[j-1] == '\r' || buf2[j-1] == '\n' ) {
		    } else{ 
			break;
		    }
		}
		buf2[j] = 0;
		int flag = 1;
		char ** list = match(buf2,depth, tokenss, flag);
		if(list == 0) {
		    count = 0;
		}  else {
		    for(int x = 0;;x++) {
			if(list[x] == 0) {
			    break;
			}
			count++;
			delete list[x];
		    }
		    delete list;
		}
		printf("Case #%d: %d\n",caseid, count);
		caseid++;
	    }
	    i++;
	}
    }
    fclose(fp);
    return 0;
}
