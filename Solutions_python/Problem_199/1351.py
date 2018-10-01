#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-08 14:41:33
# @Author  : yanbin.kang
# @Email   : yanbin.kang@yitu-inc.com


import logging
import argparse


def work(args):
    lines = []
    with open(args.input)as fd:
        for el in fd:
            lines.append(el.strip())
    case = 0
    for line in lines[1:]:
        case = case + 1
        vec = line.split()
        cake = list(vec[0])
        ll = int(vec[1])
        cnt = 0
        for i, c in enumerate(cake):
            if c == '-' and i + ll <= len(cake):
                cnt += 1
                for j in range(ll):
                    if cake[i + j] == '+':
                        cake[i + j] = '-'
                    else:
                        cake[i + j] = '+'
        flag = len(set(cake)) == 1 and cake[0] == '+'
        with open(args.output, 'a')as fd:
            if flag:
                fd.write("Case #%d: %s\n" % (case, str(cnt)))
            else:
                fd.write("Case #%d: %s\n" % (case, 'IMPOSSIBLE'))


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--input', '-i', help='input file', required=True)
    argparser.add_argument('--output', '-o', help='output file', required=True)
    args = argparser.parse_args()
    work(args)


if __name__ == '__main__':
    logging.root.setLevel(logging.INFO)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s[%(asctime)s %(filename)s:%(lineno)d]%(message)s')
    main()
