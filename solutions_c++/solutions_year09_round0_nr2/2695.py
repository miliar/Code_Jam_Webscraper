/*
 * A.h
 *
 *  Created on: Sep 2, 2009
 *      Author: Qian Xin
 */

#ifndef B_H_
#define B_H_

#include <vector>
#include <string>
#include <iostream>
#include <map>

using namespace std;

//#define m_debug

class MyCell;

class MyMap
{
public:
    vector<MyCell> cells;
    int H, W;
    int size;
    vector<int> sink_cells;
    MyMap(int inH, int intW);

    bool isvalid(int index)
    {
        return (index >= 0) && (index < size);
    }

    int get_ih(int index)
    {
        return index / W;
    }

    int get_iw(int index)
    {
        return index % W;
    }

    int getValidIndex(int index)
    {
        if (isvalid(index))
            return index;
        else
            return -1;
    }
    int getSi(int index)
    {
        return getValidIndex(index + W);
    }
    int getNi(int index)
    {
        return getValidIndex(index - W);
    }
    int getWi(int index)
    {
        int result = index - 1;
        if (get_ih(index) == get_ih(result))
            return getValidIndex(result);
        else
            return -1;
    }

    int getEi(int index)
    {
        int result = index + 1;
        if (get_ih(index) == get_ih(result))
            return getValidIndex(result);
        else
            return -1;
    }
    void dump(ostream& o);
    void dumpbasin(ostream& o);
    void walk_through();
    void whetherflow(int nb,int i);
    void paint_basin_group();
    void paint_basin(int i, int inbasin_group);
};

class MyCell
{
public:
    int latitude;

    MyMap* pmap;
    int index;
    vector<int> parent; // pay attention about shadow copy
    int child; //if child is itself, then it is suck cell;
    bool sink_cell;
    int basin_group;

    MyCell()
    {
        sink_cell = 0;
        basin_group=-1;
        pmap = NULL;
        parent.resize(0);
    }

    MyCell(MyMap* inmap, int inl, int ini)
    {
        sink_cell = 0;
        basin_group=-1;
        parent.resize(0);
        pmap = inmap;
        latitude = inl;
        index = ini;
    }

    int getS()
    {
        if (pmap)
            return pmap->getSi(index);
        else
            return -1;
    }
    int getN()
    {
        if (pmap)
            return pmap->getNi(index);
        else
            return -1;
    }
    int getW()
    {
        if (pmap)
            return pmap->getWi(index);
        else
            return -1;
    }
    int getE()
    {
        if (pmap)
            return pmap->getEi(index);
        else
            return -1;
    }
};

#endif /* A_H_ */
