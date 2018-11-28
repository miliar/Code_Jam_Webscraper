/*
 * File:   main.cpp
 * Author: Florin
 *
 * Created on September 12, 2009, 6:53 PM
 */

#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

void ident(int count)
{
    for(int i = 0; i < count; i++)
        cout<<" ";
}

class Animal
{
public:
    long featureCount;
    char** features;
    char* name;
    
    Animal(fstream& fin)
    {
        name = new char[0xF];
        fin>>name;
        
        fin>>featureCount;

        features = new char*[featureCount];

        for(long i = 0; i < featureCount; i++)
        {
            features[i] = new char[0xF];

            fin>>features[i];
        }
    }

    bool hasFeature(char* s)
    {
        if(s == NULL)
            return true;

        for(long i = 0; i < featureCount; i++)
            if(!strcmp(s, features[i]))
                return true;
        
        return false;
    }

    void print()
    {
        cout<<endl<<"Animal '"<<name<<"'";

        for(long i = 0; i < featureCount; i++)
            cout<<endl<<"\t'"<<features[i]<<"'";
    }

    ~Animal()
    {
        delete[] name;
        for(long i = 0; i < featureCount; i++)
            delete[] features[i];

        delete[] features;
    }
};

class Node
{
public:
    Node* parent;
    double weight;
    char* feature;
    Node* children[2];
    int addedChildren;

    Node(Node* parent, char* data)
    {
        this->addedChildren = 0;
        this->parent = parent;

        children[0] = NULL;
        children[1] = NULL;

        istringstream s(data);

        s>>weight;


        while(s.peek() == ' ' || s.peek() == '\t' || s.peek() == ')')
            s.seekg(1, ios::cur);
            
        if(s.peek() != EOF)
        {
            feature = new char[0xFFF];
            //cout<<endl<<"F = "<<(int)s.peek();

            s>>feature;//cout<<endl<<"FS = "<<feature;
        }
        else{//cout<<endl<<"EOF";
            feature = NULL;}
    }

    void addChild(Node* c)
    {
        children[addedChildren++] = c;
    }

    void print(int identation)
    {
        cout<<endl;ident(identation);cout<<"(";
        
        cout<<endl;ident(identation);
        cout<<"weight = "<<weight;

        if(feature)
            cout<<" feature = '"<<feature<<"'";
        
        if(children[0])
        {
            children[0]->print(identation + 4);

        }

        if(children[1])
        {
            children[1]->print(identation + 4);
        }
        
        cout<<endl;ident(identation);cout<<")";
    }

    ~Node()
    {
        if(feature)
            delete[] feature;

        if(children[0])
            delete children[0];

        if(children[1])
            delete children[1];
    }
};

class DTree
{
public:
    long L;
    Node* root;

    DTree(fstream& fin)
    {
        fin>>L;
        
        //cout<<endl<<"L = "<<L;

        Node* parent = NULL;

        char* line = new char[0xFFF];

        fin.getline(line, 0xFFF);
        
        for(long i = 0; i < L; i++)
        {
            fin.getline(line, 0xFFF);
            int k = 0;
            while(line[k] == ' ' || line[k] == '\t')
                k++;

            while(line[strlen(line) - 1] == ' ' || line[strlen(line) - 1] == '\t' || line[strlen(line) - 1] == '\n'  || line[strlen(line) - 1] == '\r')
                line[strlen(line) - 1] = 0;

            if(line[k] == '(')
            {
                Node* node = new Node(parent, &line[k + 1]);

                if(parent != NULL)
                    parent->addChild(node);
                else
                    root = node;
                
                parent = node;
            }

            while(line[strlen(line) - 1] == ')')
            {
                parent = parent->parent;
                line[strlen(line) - 1] = 0;
            }
        }
    }

    void print()
    {
        root->print(0);
    }

    ~DTree()
    {
        delete root;
    }
};

double cutep;

void solve(Animal* animal, Node* node)
{
    if(!node)
        return;
    
    cutep *= node->weight;

   if(animal->hasFeature(node->feature))
   {
        if(node->children[0])
            solve(animal, node->children[0]);
   }
   else
   {
        if(node->children[1])
            solve(animal, node->children[1]);
   }
}

int main(int argc, char** argv)
{
    try
    {
        fstream fin("D:\\codejam\\alarge.in", ios::in | ios::binary);
        fstream fo("D:\\codejam\\alarge.out", ios::out | ios::binary);

        long testCaseCount;

        fin>>testCaseCount;

        for(long testCase = 0; testCase < testCaseCount; testCase++)
        {
            cout<<endl<<"#"<<testCase;

            DTree dt(fin);

            //dt.print();

            long animalCount;
            fin>>animalCount;

            char line[0xFF];
            fin.getline(&line[0], 0xFF);

            fo<<"Case #"<<(testCase + 1)<<": "<<endl;

            for(long i = 0; i < animalCount; i++)
            {
                Animal animal(fin);

                //animal.print();

                cutep = 1;

                solve(&animal, dt.root);

                fo<<fixed<<setprecision(16)<<cutep<<endl;
            }
        }

        fin.close();
        fo.close();
    }
    catch(exception e)
    {
        cout<<endl<<"Err: "<<e.what();
    }

    return (EXIT_SUCCESS);
}

