/*
 *  joint_set.h
 *  
 *
 *  Created by Chuan-Chih Chou on 09/06/01.
 *  Copyright 2009 University of Michigan. All rights reserved.
 *
 */

#import <vector>

class joint_set
{
public:
	joint_set(int size);
	int unify(int a, int b);
	int find(int index);
	bool same(int a, int b);
	
private:
	std::vector<int> identity, rank;
};
