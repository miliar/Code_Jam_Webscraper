/*
 *  Person.cpp
 *  QualifC
 *
 *  Created by David Stockley on 08/05/2010.
 *  Copyright 2010 David Stockley. All rights reserved.
 *
 */

#include "Person.h"

Person::Person(unsigned long size, Person* linked) {
    s = size;
    l = linked;
}

unsigned long Person::getSize() {
    return s;
}

Person* Person::getNext() {
    return l;
}

void Person::setNext(Person* next) {
    l = next;
}
