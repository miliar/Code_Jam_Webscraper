#include "Defines.h"
#include "Grid.h"

using namespace std;

Grid::Grid(const N_TYPE iN)
: _n(iN > MIN_N?iN:MIN_N), _grid(_n,LINE_TYPE(_n)), _toRead(0), _ready(false)
{
}

bool Grid::Resize(const N_TYPE nN)
{
	N_TYPE usedN = 0;
	if(nN > MIN_N)
	{
		usedN = nN;
	}
	else
	{
		usedN = MIN_N;
	}
	if(usedN == _n)
	{
		return false;
	}
	_grid.resize(nN,LINE_TYPE(nN));
	_n = nN;
	_toRead = 0;
	_ready = false;
	return true;
}


bool Grid::ReadLine(string line)
{
	if(_ready || _toRead >= _n)
	{//so we've read enough already
		return false;
	}
	for(N_TYPE i = 0;i < _n;i++)
	{
		_grid.at(_toRead).at(i) = line.at(i);
	}
	if(++_toRead >= _n)
	{
		_ready = true;
	}
	return true;
}


void Grid::Rotate()
{
	_DoRotation();
	_ApplyGravity();
}


RESULT_TYPE Grid::Test(const K_TYPE& k)
{
	bool blueWon = false;
	bool redWon = false;
	bool res = false;
	ELEM_TYPE c;
	for(N_TYPE x = 0;x < _n;x++)
	{
		for(int y = _n - 1;y >= 0;y--)
		{
			c = _grid.at(y).at(x);
			if(c == EMPTY_TILE)
			{
				break;
			}
			if((c == RED_TILE && redWon) || (c == BLUE_TILE && blueWon))
			{
				continue;
			}
			res = _TestColourRight(k,x,y,c);
			if(!res)
			{
				res = _TestColourUp(k,x,y,c);
			}
			if(!res)
			{
				res = _TestColourUpRight(k,x,y,c);
			}
			if(!res)
			{
				res = _TestColourDownRight(k,x,y,c);
			}
			if(res)
			{
				if(c == RED_TILE)
				{
					redWon = true;
				}
				else if(c == BLUE_TILE)
				{
					blueWon = true;
				}
			}
		}
	}
	if(redWon)
	{
		if(blueWon)
		{
			return BOTH_WIN;
		}
		else
		{
			return RED_WIN;
		}
	}
	else
	{
		if(blueWon)
		{
			return BLUE_WIN;
		}
		else
		{
			return NO_WIN;
		}
	}
}


Grid::operator string()
{
	string res = "";
	for(N_TYPE y = 0;y < _n;y++)
	{
		for(N_TYPE x = 0;x < _n;x++)
		{
			res.append(1,_grid.at(y).at(x));
		}
		if(y < _n - 1)
		{
			res.append(1,'\n');
		}
	}
	return res;
}


void Grid::_DoRotation()
{
	vector<LINE_TYPE> copyGrid(_n,LINE_TYPE(0));
	for(N_TYPE i = 0;i < _n;i++)
	{
		copyGrid.at(i) = _grid.at(i);//copy rows
	}

	for(N_TYPE x = 0;x < _n;x++)
	{
		for(N_TYPE y = 0;y < _n;y++)
		{
			/*y,x -> y',x' (here 1-based)
			  1,1 -> 1,_n
			  _n,1 -> 1,1
			  1,_n -> _n,_n
			  _n,_n -> _n,1*/
			//_grid.at(y).at(x) = copyGrid.at(x).at((_n - 1) - y);
			_grid.at(y).at(x) = copyGrid.at((_n - 1) - x).at(y);
		}
	}
}

void Grid::_ApplyGravity()
{
	N_TYPE lowest;
	for(N_TYPE x = 0;x < _n;x++)
	{
		for(int y = _n - 1;y >= 0;y--)
		{
			lowest = _LowestFloating(x,y);
			if((int) lowest > y)
			{//so we move the tile down
				_grid.at(lowest).at(x) = _grid.at(y).at(x);
				_grid.at(y).at(x) = EMPTY_TILE;
			}
		}
	}
}

N_TYPE Grid::_LowestFloating(const N_TYPE x,const N_TYPE yMax)
{
	int y;
	for(y = _n - 1;y >= int(yMax);y--)
	{
		if(_grid.at(y).at(x) == EMPTY_TILE)
		{
			break;
		}
	}
	return y;//so if y == yMax there were no empty tiles OR it was empty; user knows here, I guess
}

bool Grid::_TestColourRight(const K_TYPE& k,const N_TYPE x,const N_TYPE y,const ELEM_TYPE c)
{
	if(_n - x < k)
	{
		return false;
	}
	for(K_TYPE i = 0;i < k;i++)
	{
		if(_grid.at(y).at(x + i) != c)
		{
			return false;
		}
	}
	return true;
}

bool Grid::_TestColourUp(const K_TYPE& k,const N_TYPE x,const N_TYPE y,const ELEM_TYPE c)
{
	if(y + 1 < k)
	{
		return false;
	}
	for(K_TYPE i = 0;i < k;i++)
	{
		if(_grid.at(y - i).at(x) != c)
		{
			return false;
		}
	}
	return true;
}

bool Grid::_TestColourUpRight(const K_TYPE& k,const N_TYPE x,const N_TYPE y,const ELEM_TYPE c)
{
	if(_n - x < k || y + 1 < k)
	{
		return false;
	}
	for(K_TYPE i = 0;i < k;i++)
	{
		if(_grid.at(y - i).at(x + i) != c)
		{
			return false;
		}
	}
	return true;
}

bool Grid::_TestColourDownRight(const K_TYPE& k,const N_TYPE x,const N_TYPE y,const ELEM_TYPE c)
{
	if(_n - x < k || _n - y < k)
	{
		return false;
	}
	for(K_TYPE i = 0;i < k;i++)
	{
		if(_grid.at(y + i).at(x + i) != c)
		{
			return false;
		}
	}
	return true;
}