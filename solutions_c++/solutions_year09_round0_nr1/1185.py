//============================================================================
// Name        : alien_language.cpp
// Author      : Kinshul Verma
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string.h>
using namespace std;

typedef struct trie{
	char alpha;
	int pos;
	struct trie * child;
	struct trie * sibling;
}trie;

trie * hashtable[26]={NULL};
int L,matches;

void insert(trie * root, char * word, int index){
	int l = strlen(word);
	trie *curr = root, *temp, *temp2;
	for(int i=1;i<l;i++){
		if(curr->child == NULL){
			temp = new trie;
			temp->child = NULL;
			temp->sibling = NULL;
			temp->alpha = word[i];
			curr->child = temp;
			curr = temp;
		}
		else{
			temp = curr->child;
			while(temp->sibling != NULL && temp->alpha != word[i]) temp=temp->sibling;
			if(temp->sibling==NULL){
				if(temp->alpha == word[i])
					curr=temp;
				else{
					temp2 = new trie;
					temp2->alpha = word[i];
					temp2->sibling = NULL;
					temp2->child = NULL;
					temp->sibling = temp2;
					curr = temp2;
				}
			}
			else{
				curr=temp;
			}
		}
	}
	trie * node = new trie;
	node->alpha = '1';
	node->pos=index;
	node->child = NULL;
	node->sibling = NULL;
	curr->child = node;
}
/*
int search(trie * root, char * word){
	int l=strlen(word);
	trie *curr = root, *temp;
	for(int i=1;i<l;i++){
		temp = curr->child;
		while(temp!=NULL && temp->alpha!=word[i])temp=temp->sibling;
		if(temp==NULL)return -1;
		curr=temp;
	}
	temp = curr->child;
	while(temp!=NULL && temp->alpha!='1')temp=temp->sibling;
	if(temp==NULL)
		return -1;
	return temp->pos;
}
*/
void memfree(trie *root){
	trie * curr = root;
	if(curr->sibling!=NULL){
			memfree(curr->sibling);
			curr->sibling=NULL; /*Not required */
	}
	if(curr->child!=NULL)
		memfree(curr->child);
	delete curr;
}
trie * search(trie *parent, char c)
{
	trie *sibling = NULL;
	if (parent == NULL)
	{
		sibling = hashtable[c - 97];
	}
	else
	{
		sibling = parent->child;
		while (sibling != NULL && sibling->alpha != c)
			sibling = sibling->sibling;
	}
	return sibling;
}
void find(char *pattern, int pos, int length, trie *parent)
{
	int i,next;
	trie *sibling;
	if(length == L)
	{
		matches++;
		return;
	}
	if(pattern[pos]=='(')
	{
		for(i=pos+1; pattern[i]!=')'; i++);
		next=i;
		for(i=pos+1; i<next; i++)
		{
			sibling = search(parent, pattern[i]);
			if(sibling!=NULL)
						find(pattern, next+1, length+1, sibling);
		}
	}
	else
	{
		sibling = search(parent, pattern[pos]);
		if(sibling!=NULL)
			find(pattern, pos+1, length+1, sibling);
	}
}

int main() {
	int D,N,i;
	scanf("%d %d %d",&L,&D,&N);
	char word[20];
	trie *root;
	for(i=0; i<D; i++)
	{
		scanf("%s",word);
		if(hashtable[word[0]-97]==NULL)
		{
			root = new trie;
			root->alpha = word[0];
			root->sibling = NULL;
			root->child = NULL;
			hashtable[word[0]-97] = root;
		}
		insert(hashtable[word[0]-97],word, i);
	}
	for(i=0; i<N; i++)
	{
		char pattern[500]={0};
		scanf("%s",pattern);
		matches = 0;
		find(pattern, 0, 0, NULL);
		printf("Case #%d: %d\n",i+1,matches);
	}
	for(i=0;i<26;i++){
			if(hashtable[i]!=NULL)memfree(hashtable[i]);
	}
	return 0;
}
