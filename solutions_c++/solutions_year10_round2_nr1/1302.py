#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
// installed "libgmp3-dev" package on ubuntu
#include <gmpxx.h>

using namespace std;

#define BUFSZ 10000


typedef map<int, char *> blahtype;

typedef struct
{
    char name[101];
    int depth;
    void *next;
    void *subdirs;
} node;


// root
node root;

node * addpath(char *name, node *parent, bool &added)
{
    node *temp = (node*)parent->subdirs;
    node * newnode;

    if (temp == NULL) // first subdirectory
    {
//        printf("adding %s\n", name);
        newnode = new node;
        parent->subdirs = (void*)newnode;
        strcpy(newnode->name, name);
        newnode->next = NULL;
        newnode->subdirs = NULL;
        added = true;
        return newnode;
    }
    while (temp != NULL)
    {
        if (strcmp(temp->name, name) == 0)
        {
//            printf("found %s\n", name);
            added = false;
            return temp;
        }
        if (temp->next == NULL) break;
        temp = (node*)temp->next;
    }

//    printf("adding next %s\n", name);
//    printf("after %s\n", temp->name);
    newnode = new node;
    temp->next = (void*)newnode;
    strcpy(newnode->name, name);
    newnode->next = NULL;
    newnode->subdirs = NULL;
    added = true;
    return newnode;
}

void delpath(node *parent)
{
    node *temp = (node*)parent->subdirs;
    node *next;

    printf("del node %s\n", temp->name);
    while (temp != NULL)
    {
        if (temp->subdirs != NULL) delpath((node *)temp->subdirs);
        if (temp->next != NULL)
        {
            next = temp;
            temp->next = NULL;
            delpath(temp);
            delpath(next);
        }
    }
}



int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int N, M;
    int i, j, k;
    long int count;

    if (argc != 2)
    {
        exit(-1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Usage: file is no good\n");
        exit(-1);
    }

    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    T = atoi(token);

    for (i=0; i<T; i++)
    {
        count = 0;
        root.next = NULL;
        root.subdirs = NULL;

        node *nodep;
        bool added;

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        subtoken = strtok_r(token, " ", &sptr2);
        N = atoi(subtoken);
        subtoken = strtok_r(NULL, " ", &sptr2);
        M = atoi(subtoken);

        for (j=0; j<N; j++)
        {
            fgets(strBuf, BUFSZ, fp);
            token = strtok_r(strBuf, "\r\n", &sptr1);


            nodep = &root;
            while (subtoken = strtok_r(token, "/", &sptr2))
            {
                nodep = addpath(subtoken, nodep, added);
                token = NULL;
            }
        }

        for (j=0; j<M; j++)
        {
            fgets(strBuf, BUFSZ, fp);
            token = strtok_r(strBuf, "\r\n", &sptr1);

            nodep = &root;

            while (subtoken = strtok_r(token, "/", &sptr2))
            {
                nodep = addpath(subtoken, nodep, added);
                if (added) count++;
                token = NULL;
            }
        }
//        delpath((node *)root.subdirs);
        root.subdirs = NULL;

        printf("Case #%d: %ld\n", i+1, count);
//        printf("asdf = %ld\n", asdf);
//        cout << "Case #" << i+1 << ": " << setiosflags(ios::fixed) << setprecision(6) << sum << "\n";
    }

    fclose(fp);
    return 0;
}
